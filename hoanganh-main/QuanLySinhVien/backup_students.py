from pymongo import MongoClient

# Kết nối đến MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Đảm bảo rằng MongoDB đang chạy
db = client["student_management"]  # Kết nối đến cơ sở dữ liệu student_management
students_collection = db["students"]  # Kết nối đến collection students

# Tên của collection sao lưu
backup_collection_name = "students_backup"
backup_collection = db[backup_collection_name]  # Kết nối đến collection sao lưu

# Xóa collection backup nếu nó đã tồn tại
backup_collection.delete_many({})  # Xóa tất cả tài liệu hiện có trong collection backup

# Truy xuất tất cả tài liệu từ collection students
try:
    students = students_collection.find()  # Lấy tất cả tài liệu từ collection students
    backup_data = []  # Danh sách để lưu trữ dữ liệu sao lưu

    for student in students:
        # Loại bỏ trường _id để tránh xung đột khi chèn vào collection backup
        student_backup = student.copy()  # Tạo bản sao của tài liệu
        student_backup.pop('_id', None)  # Xóa trường _id
        backup_data.append(student_backup)  # Thêm tài liệu vào danh sách sao lưu

    # Chèn dữ liệu vào collection backup
    if backup_data:
        backup_collection.insert_many(backup_data)  # Chèn tất cả tài liệu vào collection backup
        print(f"Backup created successfully. {len(backup_data)} documents inserted into '{backup_collection_name}'.")
    else:
        print("No documents found to backup.")

except Exception as e:
    print("Error during backup:", e)
