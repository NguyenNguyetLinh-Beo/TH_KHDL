# TH_KHDL
DỰ ÁN THỰC HÀNH
SO SÁNH HIỆU NĂNG VÀ KIẾN TRÚC PANDAS VS PYSPARK TRÊN CỤM PHÂN TÁN
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
  
Chạy PySpark ở local mode trên Windows

Yêu cầu cấu hình: Do máy yếu nên không dùng máy ảo mà chạy thẳng 

- Windows local mode
- Python
- Java
- PySpark
- Pandas
Công cụ	Quy mô dữ liệu
Pandas	1 tháng dữ liệu (~3-4 triệu dòng)
PySpark	1-2 năm dữ liệu (~40-80 triệu dòng)
