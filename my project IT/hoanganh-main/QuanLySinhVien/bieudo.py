import pandas as pd
import matplotlib.pyplot as plt

# Tạo một DataFrame mẫu cho dữ liệu sinh viên
data = {
    'Tên Sinh Viên': ['Nguyễn Văn A', 'Trần Thị B', 'Lê Văn C', 'Nguyễn Thị D', 'Trần Văn E'],
    'Ngành Học': ['Công nghệ thông tin', 'Kinh tế', 'Khoa học tự nhiên', 'Công nghệ thông tin', 'Kinh tế'],
    'Điểm Trung Bình': [8.0, 7.5, 8.5, 9.0, 6.5],
    'Khu Vực': ['Hà Nội', 'Hà Nội', 'Đà Nẵng', 'Hải Phòng', 'Hà Nội'],
    'Tham Gia Hoạt Động Ngoại Khóa': [1, 0, 1, 1, 0],
    'Nhận Học Bổng': ['Có', 'Không', 'Có', 'Có', 'Không']
}

df = pd.DataFrame(data)

# 1. Biểu đồ phân bố sinh viên theo ngành học
def plot_student_distribution_by_major(df):
    major_counts = df['Ngành Học'].value_counts()
    plt.figure(figsize=(10, 6))
    major_counts.plot(kind='bar', color='skyblue')
    plt.title('Phân bố sinh viên theo ngành học')
    plt.xlabel('Ngành học')
    plt.ylabel('Số lượng sinh viên')
    plt.xticks(rotation=45)
    plt.show()

# 2. Biểu đồ thành tích học tập
def plot_academic_performance(df):
    plt.figure(figsize=(10, 6))
    df.groupby('Ngành Học')['Điểm Trung Bình'].mean().plot(kind='bar', color='lightgreen')
    plt.title('Thành tích học tập trung bình theo ngành học')
    plt.xlabel('Ngành học')
    plt.ylabel('Điểm Trung Bình')
    plt.xticks(rotation=45)
    plt.show()

# 3. Biểu đồ phân bố sinh viên theo khu vực địa lý
def plot_student_distribution_by_region(df):    
    region_counts = df['Khu Vực'].value_counts()
    plt.figure(figsize=(10, 6))
    region_counts.plot(kind='bar', color='lightcoral')
    plt.title('Phân bố sinh viên theo khu vực địa lý')
    plt.xlabel('Khu vực')
    plt.ylabel('Số lượng sinh viên')
    plt.xticks(rotation=45)
    plt.show()

# 4. Biểu đồ tỷ lệ tham gia các hoạt động ngoại khóa
def plot_extracurricular_participation(df):
    participation_counts = df['Tham Gia Hoạt Động Ngoại Khóa'].value_counts()
    plt.figure(figsize=(10, 6))
    participation_counts.plot(kind='bar', color='gold')
    plt.title('Tỷ lệ tham gia các hoạt động ngoại khóa')
    plt.xlabel('Tham gia hoạt động ngoại khóa')
    plt.ylabel('Số lượng sinh viên')
    plt.xticks(rotation=0)
    plt.show()

# 5. Biểu đồ phân bố học bổng
def plot_scholarship_distribution(df):
    scholarship_counts = df['Nhận Học Bổng'].value_counts()
    plt.figure(figsize=(2, 9))
    scholarship_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
    plt.title('Phân bố học bổng')
    plt.ylabel('')
    plt.show()

# Gọi các hàm để vẽ biểu đồ
plot_student_distribution_by_major(df)
plot_academic_performance(df)
plot_student_distribution_by_region(df)
plot_extracurricular_participation(df)
plot_scholarship_distribution(df)
