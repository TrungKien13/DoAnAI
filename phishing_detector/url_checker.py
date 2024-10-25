# url_checker.py

class URLChecker:
    def __init__(self, db):
        self.db = db

    def check(self, url):
        # Kiểm tra URL (ví dụ: regex hoặc từ điển)
        if "malicious" in url:
            result = "URL có khả năng độc hại."
        else:
            result = "URL an toàn."

        # Log kết quả vào cơ sở dữ liệu
        self.db.log_history('url', url, result)
        return result
