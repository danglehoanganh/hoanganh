import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd


# Hàm vẽ biểu đồ phân bố sinh viên theo ngành học
def plot_student_distribution_by_major(df):
    major_counts = df['Ngành Học'].value_counts()
    plt.figure(figsize=(10, 6))
    major_counts.plot(kind='bar', color='skyblue')
    plt.title('Phân bố sinh viên theo ngành học')
    plt.xlabel('Ngành học')
    plt.ylabel('Số lượng sinh viên')
    plt.xticks(rotation=45)
    plt.show()

# Hàm vẽ biểu đồ thành tích học tập
def plot_academic_performance(df):
    plt.figure(figsize=(10, 6))
    df.groupby('Ngành Học')['Điểm Trung Bình'].mean().plot(kind='bar', color='lightgreen')
    plt.title('Thành tích học tập trung bình theo ngành học')
    plt.xlabel('Ngành học')
    plt.ylabel('Điểm Trung Bình')
    plt.xticks(rotation=45)
    plt.show()

# Hàm vẽ biểu đồ phân bố sinh viên theo khu vực địa lý
def plot_student_distribution_by_region(df):
    region_counts = df['Khu Vực'].value_counts()
    plt.figure(figsize=(10, 6))
    region_counts.plot(kind='bar', color='red')
    plt.title('Phân bố sinh viên theo khu vực địa lý')
    plt.xlabel('Khu vực')
    plt.ylabel('Số lượng sinh viên')
    plt.xticks(rotation=45)
    plt.show()

# Hàm vẽ biểu đồ tỷ lệ tham gia các hoạt động ngoại khóa
def plot_extracurricular_participation(df):
    participation_counts = df['Tham Gia Hoạt Động Ngoại Khóa'].value_counts()
    plt.figure(figsize=(13, 9))
    participation_counts.plot(kind='bar', color='gold')
    plt.title('Tỷ lệ tham gia các hoạt động ngoại khóa')
    plt.xlabel('Tham gia hoạt động ngoại khóa')
    plt.ylabel('Số lượng sinh viên')
    plt.xticks(rotation=0)
    plt.show()

# Hàm vẽ biểu đồ phân bố học bổng
def plot_scholarship_distribution(df):
    scholarship_counts = df['Nhận Học Bổng'].value_counts()
    plt.figure(figsize=(19, 23))
    scholarship_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','blue'])
    plt.title('Phân bố học bổng')
    plt.ylabel('')
    plt.show()

# Hàm hiển thị menu và lấy lựa chọn từ người dùng
def menu():
    while True:
        print("\n=== Hệ thống quản lý sinh viên ===")
        print("1. Biểu đồ phân bố sinh viên theo ngành học")
        print("2. Biểu đồ thành tích học tập")
        print("3. Biểu đồ phân bố sinh viên theo khu vực địa lý")
        print("4. Biểu đồ tỷ lệ tham gia các hoạt động ngoại khóa")
        print("5. Biểu đồ phân bố học bổng")
        print("0. Thoát")

        choice = input("Chọn biểu đồ bạn muốn xem (0-5): ")

        if choice == '1':
            plot_student_distribution_by_major(df)
        elif choice == '2':
            plot_academic_performance(df)
        elif choice == '3':
            plot_student_distribution_by_region(df)
        elif choice == '4':
            plot_extracurricular_participation(df)
        elif choice == '5':
            plot_scholarship_distribution(df)
        elif choice == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Tạo DataFrame mẫu cho dữ liệu sinh viên
data = {
    'Tên Sinh Viên': ['Nguyễn Văn A', 'Trần Thị B', 'Lê Văn C', 'Nguyễn Thị D', 'Trần Văn E'],
    'Ngành Học': ['Công nghệ thông tin', 'Kinh tế', 'Khoa học tự nhiên', 'Công nghệ thông tin', 'Kinh tế'],
    'Điểm Trung Bình': [8.0, 7.5, 8.5, 9.0, 6.5],
    'Khu Vực': ['Hà Nội', 'Hà Nội', 'Đà Nẵng', 'Hải Phòng', 'Hà Nội'],
    'Tham Gia Hoạt Động Ngoại Khóa': [1, 0, 1, 1, 0],
    'Nhận Học Bổng': ['Có', 'Không', 'Có', 'Có', 'Không']
}

df = pd.DataFrame(data)

# Gọi hàm menu để chạy chương trình
menu()

from pymongo import MongoClient

# Kết nối đến MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Đảm bảo rằng MongoDB đang chạy
db = client["student_management"]  # Kết nối đến cơ sở dữ liệu student_management
students_collection = db["students"]  # Kết nối đến collection students

# Danh sách sinh viên để thêm vào MongoDB
students = [
    {
        "name": "Nguyen Van A",
        "major": "Computer Science",
        "gpa": 3.8,
        "address": {
            "city": "Hanoi",
            "district": "Dong Da"
        },
        "activities": ["Coding Club", "Robotics Club"]
    },
    {
        "name": "Tran Thi B",
        "major": "Mathematics",
        "gpa": 3.9,
        "address": {
            "city": "Ho Chi Minh City",
            "district": "District 1"
        },
        "activities": ["Math Club", "Chess Club"]
    },
    {
        "name": "Le Van C",
        "major": "Physics",
        "gpa": 3.7,
        "address": {
            "city": "Da Nang",
            "district": "Hai Chau"
        },
        "activities": ["Physics Society", "Basketball Team"]
    }
]

# Thêm tất cả tài liệu vào collection
try:
    # Xóa tất cả tài liệu hiện có (nếu cần)
    students_collection.delete_many({})  # Xóa nếu cần
    result = students_collection.insert_many(students)
    print("Documents inserted with IDs:", result.inserted_ids)
except Exception as e:
    print("Error inserting documents:", e)

# Truy xuất tất cả tài liệu trong collection
try:
    students = students_collection.find()  # Lấy tất cả tài liệu
    print("\nCurrent documents in 'students' collection:")
    
    for student in students:
        print(student)  # In từng tài liệu ra màn hình
except Exception as e:
    print("Error retrieving documents:", e)








