import pandas as pd
import time

# Bắt đầu tính thời gian
start_time = time.time()

print("Đang đọc dữ liệu bằng Pandas...")

# Đọc file parquet
file_path = "data/taxi_data.parquet"

pdf = pd.read_parquet(file_path)

print("Đọc dữ liệu thành công!")

# Tính thời gian chuyến đi
pdf['trip_duration_mins'] = (
    pdf['tpep_dropoff_datetime']
    - pdf['tpep_pickup_datetime']
).dt.total_seconds() / 60

# Lấy giờ đón khách
pdf['pickup_hour'] = pdf['tpep_pickup_datetime'].dt.hour

# Gom nhóm dữ liệu
hourly_stats = pdf.groupby('pickup_hour').agg(
    avg_revenue=('total_amount', 'mean'),
    avg_duration=('trip_duration_mins', 'mean'),
    total_trips=('VendorID', 'count')
).reset_index()

# Sắp xếp
hourly_stats = hourly_stats.sort_values(by='pickup_hour')

# Kết thúc tính thời gian
end_time = time.time()

# Hiển thị kết quả
print("\n===== KẾT QUẢ PANDAS =====")
print(hourly_stats)

print(
    f"\nThời gian xử lý Pandas: "
    f"{end_time - start_time:.2f} giây"
)