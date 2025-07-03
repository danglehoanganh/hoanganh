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
🔐 Secure File Transfer System
Một hệ thống truyền tệp an toàn sử dụng các kỹ thuật mã hóa, chữ ký số và xác thực toàn vẹn để bảo vệ dữ liệu trong quá trình gửi và nhận. Ứng dụng có giao diện web đơn giản bằng Flask để thực hiện các bước bảo mật một cách tự động.

🚀 Chức năng chính
Mã hóa nội dung bằng DES (Data Encryption Standard)

Chia nhỏ tệp thành 3 phần và bảo vệ từng phần riêng biệt

Tạo và sử dụng RSA 1024-bit để mã hóa khóa phiên và chữ ký số

Xác thực toàn vẹn với SHA-512

Giao diện web dễ sử dụng với Flask

🗂 Cấu trúc thư mục
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
│   ├── sender_*.pem
│   └── receiver_*.pem
├── parts/                 # Chứa các phần của file đã chia và mã hóa
└── assignment_received.txt # File sau khi nhận và khôi phục


⚙️ Hướng dẫn chạy
1. Cài đặt môi trường
   pip install -r requirements.txt
Yêu cầu chính:
pycryptodome
flask

2. Khởi động hệ thống
   python app.py
Sau đó truy cập trình duyệt tại http://your_ip/
3. Các thao tác chính
Generate Keys: Sinh khóa RSA cho sender và receiver
Create Assignment: Tạo file assignment.txt gốc
Encrypt & Split: Mã hóa và chia nhỏ file thành 3 phần
Decrypt & Merge: Kiểm tra, xác minh và hợp nhất lại file

📄 Nội dung bài tập (assignment.txt)
Assignment: Secure File Transfer System

Objectives:
1. Encrypt the file using DES.
2. Sign and share the session key using RSA 1024-bit.
3. Verify integrity using SHA-512.
4. Divide the file into 3 parts and package each securely.

Deadline: May 15, 2025

📌 Ghi chú
Dự án sử dụng mã hóa đối xứng (DES) và bất đối xứng (RSA) kết hợp.
Quá trình ký số và xác minh chữ ký đảm bảo dữ liệu không bị chỉnh sửa.
Phần mềm mô phỏng việc gửi và nhận dữ liệu trong môi trường giả lập (offline).

## 📫 Liên hệ
- **Email:** [danglehoanganh0223@gmail.com]
- **GitHub:** [https://github.com/danglehoanganh/hoanganh)
