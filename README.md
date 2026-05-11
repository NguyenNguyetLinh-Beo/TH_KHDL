# TH_KHDL
# Sinh Viên
# Họ tên: Nguyễn Nguyệt Linh
# MSV: K225480106039
# Lớp: 58KTPM
# Môn: Khoa Học Dữ Liệu
# DỰ ÁN THỰC HÀNH
# SO SÁNH HIỆU NĂNG VÀ KIẾN TRÚC PANDAS VS PYSPARK TRÊN CỤM PHÂN TÁN
1. ĐẶT VẤN ĐỀ VÀ MỤC TIÊU DỰ ÁN
1.1. Bối cảnh

Trong thời đại dữ liệu lớn (Big Data), khối lượng dữ liệu sinh ra mỗi ngày ngày càng tăng mạnh. Các doanh nghiệp và tổ chức cần những công cụ có khả năng xử lý dữ liệu hiệu quả để phục vụ cho việc phân tích và ra quyết định.

Trong Python, hai công cụ phổ biến dùng để xử lý dữ liệu dạng bảng là:

- Pandas
- Apache Spark với API PySpark

Mặc dù cú pháp thao tác dữ liệu của Pandas và PySpark khá giống nhau như:

- Chọn cột
- Lọc dữ liệu
- Gom nhóm dữ liệu
- Tính toán thống kê

Nhưng bản chất kiến trúc hoạt động của chúng hoàn toàn khác nhau:

- Pandas hoạt động theo mô hình xử lý trên một máy tính duy nhất (Single Node).
- PySpark có khả năng xử lý phân tán dữ liệu trên nhiều máy tính thông qua Apache Spark. 
Trong phạm vi dự án này, hệ thống được triển khai ở chế độ Local Mode trên một máy tính cá nhân thông qua Command Prompt (CMD) của Windows để mô phỏng cơ chế xử lý dữ liệu lớn.

Do đó, dự án này được xây dựng nhằm giúp sinh viên hiểu rõ sự khác biệt về:

- Kiến trúc hệ thống
- Cơ chế thực thi
- Hiệu năng xử lý
- Khả năng mở rộng dữ liệu
1.2. Mục tiêu dự án

Dự án yêu cầu xây dựng hệ thống xử lý dữ liệu chuyến đi Taxi tại New York nhằm tính toán:

- Doanh thu trung bình theo từng giờ
- Thời gian di chuyển trung bình theo từng giờ
- Tổng số chuyến đi trong ngày

Qua dự án này, sinh viên đạt được các mục tiêu:

1. Phân biệt kiến trúc xử lý dữ liệu

Hiểu rõ:

- Giới hạn xử lý In-memory của Pandas
- Cơ chế phân tán Distributed của Spark
2. Hiểu cơ chế thực thi

So sánh:

- Eager Execution trong Pandas
- Lazy Evaluation trong PySpark

3. Kỹ năng triển khai môi trường xử lý dữ liệu lớn

- Cài đặt môi trường Java và PySpark
- Cấu hình Spark chạy ở chế độ Local Mode
- Thực thi chương trình thông qua Command Prompt (CMD)
- Theo dõi và đánh giá quá trình xử lý dữ liệu bằng Spark
4. Đánh giá hiệu năng

So sánh:

- Tốc độ xử lý
- Khả năng mở rộng
- Mức sử dụng RAM
- Độ ổn định hệ thống
1.3. Nguồn dữ liệu

Dự án sử dụng bộ dữ liệu:

- New York City Taxi and Limousine Commission

Bộ dữ liệu:

- NYC TLC Yellow Taxi Trip Records
  
Định dạng: Parquet

Nguồn tải:

- NYC TLC Trip Record Data

Quy mô dữ liệu thử nghiệm

- PySpark	1 tháng dữ liệu thử nghiệm chạy trên Local Mode

Yêu cầu cấu hình: Do máy yếu nên không dùng máy ảo mà chạy thẳng 

- Chạy PySpark ở local mode trên Windows
- Python
- Java
- PySpark
- Pandas
##GIAI ĐOẠN 1 — CHUẨN BỊ MÔI TRƯỜNG
## Bước 1 — Kiểm tra Python
<img width="765" height="139" alt="image" src="https://github.com/user-attachments/assets/6fe9d779-c605-40ac-8b93-4963f04b1820" />

###  Bước 2 — Cài Java 11
<img width="1319" height="917" alt="image" src="https://github.com/user-attachments/assets/7108eaad-5b36-4d75-a511-1f8920216fda" />

###  Bước 3 — Tạo thư mục dự án

C:\Users\nguye\BigData_Project\data
<img width="808" height="360" alt="image" src="https://github.com/user-attachments/assets/3041d51a-2a25-4e71-8d49-7e416b203f64" />

Trong đó tạo:

BigData_Project/  
│  
├── data/   
├── pandas_taxi.py  
├── pyspark_taxi.py  
├── screenshots/  
└── report/  
### Bước 4 — Cài thư viện Python
- pip install pandas pyspark pyarrow matplotlib
  <img width="1453" height="845" alt="image" src="https://github.com/user-attachments/assets/296b54f8-ad3e-4e75-8fe0-8f3f5ffeb470" />

## GIAI ĐOẠN 2 — TẢI DỮ LIỆU TAXI
Bước 5 — Tải dữ liệu
- NYC TLC Trip Record Data: yellow_tripdata_2024-01.parquet
GIAI ĐOẠN 3 — CODE PANDAS
Bước 6 — Tạo file pandas_taxi.py sau đó chạy
<img width="1476" height="880" alt="image" src="https://github.com/user-attachments/assets/c0242e51-9236-4b71-962b-a3d73919de81" />

<img width="931" height="775" alt="image" src="https://github.com/user-attachments/assets/f91d82b4-fcbc-499d-9d22-760c7c52f475" />

<img width="1783" height="859" alt="image" src="https://github.com/user-attachments/assets/c192e07b-9214-40f2-8ce5-882d066d1255" />

## GIAI ĐOẠN 4 — CODE PYSPARK
### Bước 7 — Tạo file pyspark_taxi.py sau đó chạy
<img width="1473" height="499" alt="image" src="https://github.com/user-attachments/assets/5a6ba028-d61d-41ca-9a26-309fa923c651" />

### Bước 8 — Nhận xét
- Pandas: Khởi động nhanh, Dễ dùng, RAM tăng mạnh, Phù hợp dữ liệu nhỏ
- PySpark: Khởi động chậm hơn, Xử lý song song, Ổn định với dữ liệu lớn, Có Lazy Evaluation
### Bước 9: Giải thích Lazy Evaluation theo ý hiểu của em:
- Trong PySpark: Các Transformation chưa chạy ngay, Spark tạo DAG, chỉ thực thi khi gọi Action như: .show()
