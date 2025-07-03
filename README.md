# 📂 Portfolio Projects - Dang Le Hoang Anh

Chào mừng bạn đến với trang tổng hợp các dự án cá nhân mà tôi đã thực hiện trong quá trình học và rèn luyện kỹ năng lập trình.

---

## 🎬 Movie Website - Online Platform (4/2024 - 9/2024)

**Tech Stack:** HTML, CSS, JavaScript, ReactJS  
**Role:** Frontend Developer (Solo)

### ✅ Tính năng:
- Website xem phim với tốc độ tải nhanh, responsive trên mọi thiết bị
- Giao diện dễ sử dụng, thân thiện với người dùng
- Xử lý lỗi bằng React Error Boundaries

### 🏆 Kết quả:
- Phát triển website với trải nghiệm người dùng tốt và hiệu suất cao
- Giải quyết các vấn đề về phản hồi mã bằng cách implement error boundaries

---

## 🎓 Student Management App with Data Technology (9/2024 - 10/2024)

**Tech Stack:** Python, MongoDB (Backend), HTML/CSS/JS (Frontend)  
**Role:** Developer (Team 2 người)

### ✅ Tính năng:
- Ứng dụng biểu đồ quản lý sinh viên, tối ưu hóa tốc độ truy xuất dữ liệu
- Thiết kế database tối ưu cho việc truy vấn
- Giao diện hiển thị dữ liệu rõ ràng, dễ theo dõi

### 🏆 Kết quả:
- Xây dựng thành công hệ thống giúp giảm thời gian tra cứu thông tin sinh viên
- Thiết kế cấu trúc database hiệu quả, dễ mở rộng

---

## 🔥 Giới thiệu bản thân

Tôi đam mê phát triển Frontend và luôn cố gắng nâng cao kỹ năng qua các dự án thực tế.  
Hiện tại tôi tiếp tục học hỏi và thực hành với ReactJS và các công nghệ liên quan.

---
# 🔐 Secure File Transfer System

Hệ thống truyền tệp an toàn sử dụng mã hóa đối xứng (DES), mã hóa khóa phiên và chữ ký số bằng RSA, xác minh toàn vẹn với SHA-512. Ứng dụng này có giao diện web đơn giản bằng Flask để thao tác gửi – nhận tệp bảo mật nhanh chóng.

---

## 📌 Mục tiêu

- ✅ Mã hóa file bằng DES
- ✅ Chia file thành 3 phần, mỗi phần được mã hóa, ký và lưu riêng
- ✅ Sử dụng RSA 1024-bit để mã hóa khóa phiên và ký dữ liệu
- ✅ Kiểm tra toàn vẹn bằng SHA-512
- ✅ Tái hợp file sau khi xác minh chữ ký và nội dung

---

## 🖼 Giao diện Web

Ứng dụng Flask có giao diện đơn giản gồm các nút để:
- Generate Keys
- Create Assignment
- Encrypt & Split
- Decrypt & Merge

---

## 🗂 Cấu trúc thư mục

```bash
.
├── app.py                 # Flask Web App
├── assignment.txt         # File gốc cần truyền (có thể tạo bằng create_assignment.py)
├── create_assignment.py   # Tạo file assignment.txt mẫu
├── crypto_utils.py        # Hàm hỗ trợ mã hóa/giải mã & ký số
├── generate_keys.py       # Sinh khóa RSA cho sender & receiver
├── sender.py              # Gửi file: mã hóa + ký + chia phần
├── receiver.py            # Nhận file: xác minh + giải mã + ghép file
├── style.css              # CSS cho giao diện web
├── templates/
│   └── index.html         # Giao diện chính (yêu cầu thêm)
├── keys/                  # Chứa khóa RSA
│   ├── sender_private.pem
│   ├── sender_public.pem
│   ├── receiver_private.pem
│   └── receiver_public.pem
├── parts/                 # Chứa các phần của file đã chia và mã hóa
└── assignment_received.txt # File sau khi nhận và khôi phục
```bash


⚙️ Cách sử dụng
1. Cài đặt thư viện
pip install pycryptodome flask

2. Chạy ứng dụng Flask
python app.py
Truy cập: http://your_ip

3. Các bước sử dụng trên giao diện
Generate Keys: Tạo khóa RSA cho sender và receiver
Create Assignment: Tạo file assignment.txt để truyền
Encrypt & Split: Mã hóa file, chia thành 3 phần, ký và lưu
Decrypt & Merge: Kiểm tra chữ ký, giải mã, ghép lại thành assignment_received.txt

📌 Ghi chú kỹ thuật
DES dùng CBC mode với padding thủ công
RSA 1024-bit dùng cho cả mã hóa và chữ ký
SHA-512 dùng để kiểm tra toàn vẹn nội dung từng phần
Dữ liệu chia 3 phần lưu vào các file .json kèm IV, mã hóa, hash và chữ ký

✅ Trạng thái
 Xây dựng thành công
 Giao diện Flask hoạt động
 Chưa triển khai kết nối mạng thực (hiện là mô phỏng local)


## 📫 Liên hệ
- **Email:** [danglehoanganh0223@gmail.com]
- **GitHub:** [https://github.com/danglehoanganh/hoanganh)
