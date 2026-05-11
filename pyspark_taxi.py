import os
import time
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

# ======================
# FIX WINDOWS ENV
# ======================
os.environ["PYSPARK_PYTHON"] = "python"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python"
os.environ["PYTHONHASHSEED"] = "0"

# ⚠️ ép JVM ổn định hơn trên Windows
os.environ["JAVA_OPTS"] = "-Xms512m -Xmx2g"

# ======================
# START TIMER
# ======================
start_time = time.time()

print("Đang khởi tạo Spark...")

# ======================
# SPARK SESSION (STABLE MODE)
# ======================
spark = SparkSession.builder \
    .appName("TaxiAnalysis") \
    .master("local[1]") \
    .config("spark.driver.memory", "2g") \
    .config("spark.executor.memory", "2g") \
    .config("spark.sql.shuffle.partitions", "1") \
    .config("spark.default.parallelism", "1") \
    .config("spark.ui.showConsoleProgress", "false") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print("Spark khởi tạo thành công!")

# ======================
# DATA PATH (ĐÃ CHECK OK)
# ======================
file_path = "data/taxi_data.parquet"

print("Đang đọc dữ liệu...")

# ======================
# READ DATA
# ======================
sdf = spark.read.parquet(file_path)

# ======================
# FEATURE ENGINEERING
# ======================
sdf = sdf.withColumn(
    "trip_duration_mins",
    (
        F.col("tpep_dropoff_datetime").cast("long")
        - F.col("tpep_pickup_datetime").cast("long")
    ) / 60
)

sdf = sdf.withColumn(
    "pickup_hour",
    F.hour("tpep_pickup_datetime")
)

# ======================
# AGGREGATION
# ======================
hourly_stats = sdf.groupBy("pickup_hour").agg(
    F.mean("total_amount").alias("avg_revenue"),
    F.mean("trip_duration_mins").alias("avg_duration"),
    F.count("*").alias("total_trips")
).orderBy("pickup_hour")

print("\n===== KẾT QUẢ PYSPARK =====")

hourly_stats.show(24)

# ======================
# END TIME
# ======================
end_time = time.time()

print(f"\nThời gian xử lý PySpark: {end_time - start_time:.2f} giây")

spark.stop()