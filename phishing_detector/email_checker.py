# email_checker.py

class EmailChecker:
    def __init__(self, db):
        self.db = db

    def check(self, email):
        # Kiểm tra email (ví dụ: regex hoặc từ điển)
        if "spam" in email.lower():
            result = "Email có khả năng là spam."
        else:
            result = "Email an toàn."

        # Log kết quả vào cơ sở dữ liệu
        self.db.log_history('email', email, result)
        return result
