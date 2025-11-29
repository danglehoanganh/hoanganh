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


---bash
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

---

⚙️ Cách sử dụng
1. Cài đặt thư viện
pip install pycryptodome flask
---
2. Chạy ứng dụng Flask
python app.py
Truy cập: http://your_ip
---
3. Các bước sử dụng trên giao diện
Generate Keys: Tạo khóa RSA cho sender và receiver
Create Assignment: Tạo file assignment.txt để truyền
Encrypt & Split: Mã hóa file, chia thành 3 phần, ký và lưu
Decrypt & Merge: Kiểm tra chữ ký, giải mã, ghép lại thành assignment_received.txt
---
📌 Ghi chú kỹ thuật
DES dùng CBC mode với padding thủ công
RSA 1024-bit dùng cho cả mã hóa và chữ ký
SHA-512 dùng để kiểm tra toàn vẹn nội dung từng phần
Dữ liệu chia 3 phần lưu vào các file .json kèm IV, mã hóa, hash và chữ ký
---
✅ Trạng thái
 Xây dựng thành công
 Giao diện Flask hoạt động
 Chưa triển khai kết nối mạng thực (hiện là mô phỏng local)
---

# Hệ Thống Quản Lý Lịch Tập Cá Nhân Hóa
**Next.js – Node.js/Express – MongoDB – Theo dõi tiến trình tập luyện**

## 1. Giới thiệu

Dự án này được xây dựng trong môn *Chuyển đổi số*, hướng đến việc hỗ trợ người dùng tạo lịch tập cá nhân hóa dựa trên:
- Mức độ tập luyện,
- Mục tiêu (giảm cân, tăng cơ, duy trì),
- Cường độ vận động,
- Theo dõi tiến trình theo thời gian.

Hệ thống bao gồm frontend Next.js, backend Node.js/Express và cơ sở dữ liệu MongoDB.

---

## 2. Chức năng chính

### 2.1 Xác thực & người dùng
- Đăng ký / đăng nhập bằng JWT
- Lưu thông tin cá nhân và BMI
- Phân loại người dùng: Beginner, Regular, Athlete

### 2.2 Tự động sinh lịch tập
Lịch tập được tạo dựa trên:
- Mức độ người dùng
- Mục tiêu tập luyện
- Cường độ bài tập
- Cơ sở dữ liệu bài tập có sẵn

Bao gồm:
- Sets
- Reps
- Rest time
- Lịch theo ngày/tuần

### 2.3 Theo dõi tiến trình
- Calories đốt theo ngày/tuần/tháng
- Số buổi tập hoàn thành
- Biểu đồ trực quan bằng Recharts/Chart.js
- Đồng bộ hóa thời gian thực

### 2.4 Chỉnh sửa lịch tập
- Thêm/xóa bài tập
- Điều chỉnh trọng số: reps, sets, thời gian nghỉ
- Dữ liệu được cập nhật qua API PATCH
- Giao diện trực quan dễ sử dụng

---

## 3. Kiến trúc hệ thống

### 3.1 Frontend – Next.js
- SSR + CSR kết hợp
- TailwindCSS giao diện
- Axios gọi API
- React Hooks quản lý trạng thái

### 3.2 Backend – Node.js/Express
Các module chính:
- `/api/auth`: đăng ký, đăng nhập, JWT
- `/api/users`: quản lý người dùng
- `/api/plans`: sinh lịch tập
- `/api/stats`: thống kê calories & tiến độ

Bao gồm:
- Middleware bảo mật JWT
- Mongoose Schema
- Joi validation
- Xử lý lỗi

### 3.3 Database – MongoDB
Các collection chính:
- Users
- Exercises
- WorkoutPlans
- Stats

---

## 4. Thuật toán tính cường độ


**LevelFactor:**
- Beginner: 0.8  
- Regular: 1.0  
- Athlete: 1.2  

**GoalFactor:**
- Giảm cân: 1.1  
- Tăng cơ: 1.2  
- Duy trì: 1.0  

Thuật toán đảm bảo mỗi người dùng được gợi ý bài tập phù hợp khả năng.

---

## 5. Đánh giá & kết quả

### 5.1 Kết quả kiểm thử hệ thống

| Chức năng | Tỷ lệ thành công | Độ trễ (ms) | Độ đồng bộ |
|----------|------------------|-------------|-------------|
| Đăng ký | 100% | 120ms | 99.8% |
| Đăng nhập | 100% | 115ms | 99.6% |
| Sinh lịch tập | 98.5% | 95ms | 99.2% |
| Biểu đồ tiến độ | 100% | 85ms | 100% |
| Chỉnh sửa lịch tập | 97.2% | 110ms | 98.8% |

### 5.2 Throughput Backend

| API | Requests/sec | Latency |
|-----|--------------|---------|
| /api/auth/login | 38.7 | 124ms |
| /api/plans/generate | 32.4 | 136ms |
| /api/stats/progress | 42.1 | 118ms |
| /api/users/update | 35.9 | 127ms |

### 5.3 Độ chính xác phân loại người dùng
- Accuracy trung bình: **96.7%**

---

## 6. Cấu trúc dự án (tham khảo)

/frontend
/components
/pages
/styles
/backend
/routes
/controllers
/models
/middleware
/docs
.env.example
README.md


---

# 7. Portfolio Projects

### Hệ thống quản lý lịch tập cá nhân hóa
Ứng dụng full-stack hỗ trợ người dùng:
- sinh lịch tập tự động,
- theo dõi calories,
- chỉnh sửa bài tập,
- xem thống kê trực quan bằng biểu đồ.



---

## 8. Định hướng phát triển
- Thêm AI gợi ý lịch tập tự động
- Ứng dụng mobile (React Native / Flutter)
- Tích hợp dữ liệu từ smartwatch
- Thêm tính năng cộng đồng

---

## Thông tin liên hệ

- **Email:** danglehoanganh0223@gmail.com
- **GitHub:** [https://github.com/danglehoanganh/hoanganh)



