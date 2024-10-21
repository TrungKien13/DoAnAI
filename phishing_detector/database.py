import pyodbc

class Database:
    def __init__(self):
        # Kết nối đến cơ sở dữ liệu
        self.connection = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=LAPTOP-2PTIGU9P\\SQLEXPRESS;DATABASE=PhishingDB;Trusted_Connection=yes;'
        )
        self.cursor = self.connection.cursor()  # Khởi tạo cursor sau khi kết nối thành công

    def fetch_emails(self):
        self.cursor.execute("SELECT EmailContent FROM Emails")
        return self.cursor.fetchall()  # Trả về danh sách các email

    def fetch_urls(self):
        self.cursor.execute("SELECT URLContext FROM URLs")
        return self.cursor.fetchall()  # Trả về danh sách các URL

    def fetch_history(self):
        self.cursor.execute("SELECT * FROM History ORDER BY timestamp DESC")  # Chú ý sử dụng đúng tên cột
        return self.cursor.fetchall()  # Trả về lịch sử kiểm tra

    def insert_url(self, url, result):
        self.cursor.execute("INSERT INTO URLs (URLContext, Result) VALUES (?, ?)", (url, result))
        self.connection.commit()  # Lưu thay đổi vào DB

    def close(self):
        self.cursor.close()  # Đóng cursor khi không còn sử dụng
        self.connection.close()  # Đóng kết nối
