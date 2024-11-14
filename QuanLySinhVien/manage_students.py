from pymongo import MongoClient

# Kết nối đến MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Đảm bảo rằng MongoDB đang chạy
db = client["student_management"]  # Tạo hoặc kết nối đến cơ sở dữ liệu
students_collection = db["students"]  # Tạo hoặc kết nối đến collection 'students'

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
