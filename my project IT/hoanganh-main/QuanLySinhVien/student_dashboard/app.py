from flask import Flask, render_template, send_from_directory, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import os
from pymongo import MongoClient

# Khởi tạo Flask
app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Đường dẫn lưu biểu đồ
CHART_DIR = os.path.join(app.static_folder, 'charts')
if not os.path.exists(CHART_DIR):
    os.makedirs(CHART_DIR)

# Kết nối MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["student_management"]
students_collection = db["students"]

# Dữ liệu mẫu
data = {
    'Tên Sinh Viên': ['Nguyễn Văn A', 'Trần Thị B', 'Lê Văn C', 'Nguyễn Thị D', 'Trần Văn E'],
    'Ngành Học': ['Công nghệ thông tin', 'Kinh tế', 'Khoa học tự nhiên', 'Công nghệ thông tin', 'Kinh tế'],
    'Điểm Trung Bình': [8.0, 7.5, 8.5, 9.0, 6.5],
    'Khu Vực': ['Hà Nội', 'Hà Nội', 'Đà Nẵng', 'Hải Phòng', 'Hà Nội'],
    'Tham Gia Hoạt Động Ngoại Khóa': [1, 0, 1, 1, 0],
    'Nhận Học Bổng': ['Có', 'Không', 'Có', 'Có', 'Không']
}
df = pd.DataFrame(data)

# Hàm lưu biểu đồ vào file
def save_chart(fig, filename):
    filepath = os.path.join(CHART_DIR, filename)
    fig.savefig(filepath, bbox_inches='tight')
    plt.close(fig)

# Trang chính
@app.route('/')
def index():
    return render_template('index.html')

# API tạo và hiển thị biểu đồ
@app.route('/generate/<chart_type>')
def generate_chart(chart_type):
    fig, ax = plt.subplots(figsize=(10, 6))

    if chart_type == 'major':
        df['Ngành Học'].value_counts().plot(kind='bar', color='skyblue', ax=ax)
        ax.set_title('Phân bố sinh viên theo ngành học')
        ax.set_xlabel('Ngành học')
        ax.set_ylabel('Số lượng sinh viên')
        ax.tick_params(axis='x', rotation=45)
        save_chart(fig, 'major.png')

    elif chart_type == 'performance':
        df.groupby('Ngành Học')['Điểm Trung Bình'].mean().plot(kind='bar', color='lightgreen', ax=ax)
        ax.set_title('Thành tích học tập trung bình theo ngành học')
        ax.set_xlabel('Ngành học')
        ax.set_ylabel('Điểm Trung Bình')
        ax.tick_params(axis='x', rotation=45)
        save_chart(fig, 'performance.png')

    elif chart_type == 'region':
        df['Khu Vực'].value_counts().plot(kind='bar', color='red', ax=ax)
        ax.set_title('Phân bố sinh viên theo khu vực địa lý')
        ax.set_xlabel('Khu vực')
        ax.set_ylabel('Số lượng sinh viên')
        ax.tick_params(axis='x', rotation=45)
        save_chart(fig, 'region.png')

    elif chart_type == 'activities':
        df['Tham Gia Hoạt Động Ngoại Khóa'].value_counts().plot(kind='bar', color='gold', ax=ax)
        ax.set_title('Tỷ lệ tham gia hoạt động ngoại khóa')
        ax.set_xlabel('Tham gia hoạt động')
        ax.set_ylabel('Số lượng sinh viên')
        ax.tick_params(axis='x', rotation=0)
        save_chart(fig, 'activities.png')

    elif chart_type == 'scholarship':
        fig, ax = plt.subplots(figsize=(8, 8))
        df['Nhận Học Bổng'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax,
                                                colors=['#ff9999', 'blue'])
        ax.set_title('Phân bố học bổng')
        ax.set_ylabel('')
        save_chart(fig, 'scholarship.png')

    return send_from_directory(CHART_DIR, f'{chart_type}.png')

# API lấy danh sách sinh viên từ MongoDB
@app.route('/students')
def list_students():
    try:
        students = list(students_collection.find({}, {"_id": 0}))
        return jsonify(students)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Chạy app
if __name__ == '__main__':
    app.run(debug=True)
