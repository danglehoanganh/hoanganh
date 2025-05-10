from pymongo import MongoClient

# Kết nối đến MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Đảm bảo rằng MongoDB đang chạy
db = client["student_management"]  # Kết nối đến cơ sở dữ liệu student_management
students_collection = db["students"]  # Kết nối đến collection students

# Truy xuất tất cả tài liệu trong collection
try:
    students = students_collection.find()  # Lấy tất cả tài liệu
    print("Current documents in 'students' collection:")
    
    for student in students:
        print(student)  # In từng tài liệu ra màn hình
except Exception as e:
    print("Error retrieving documents:", e)
