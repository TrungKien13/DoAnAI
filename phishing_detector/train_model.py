import pandas as pd
from database import Database
from phishing_model import PhishingModel


def create_and_train_model():
    # Kết nối đến cơ sở dữ liệu
    db = Database()

    # Lấy dữ liệu từ bảng Emails
    emails = db.fetch_emails()
    if not emails:
        print("Không có dữ liệu email nào.")
        return

    # Tạo danh sách nội dung email và nhãn
    email_contents = [email[0] for email in emails]  # Đảm bảo lấy email đúng cột
    email_labels = [0] * 99 + [1] * (len(email_contents) - 99)  # Nhãn: 0 cho an toàn, 1 cho độc hại


    # Lấy dữ liệu từ bảng URLs
    urls = db.fetch_urls()
    # Tạo danh sách nội dung URL và nhãn
    url_contents = [url[1] for url in urls]  # url[1] chứa URLContext
    url_labels = [0] * 136 + [1] * (len(url_contents) - 136)  # Nhãn: 0 cho an toàn, 1 cho độc hại

    # Kết hợp email và URL
    all_contents = email_contents + url_contents
    all_labels = email_labels + url_labels

    # Khởi tạo mô hình
    model = PhishingModel()

    # Huấn luyện mô hình với dữ liệu
    model.train(all_contents, all_labels)

    # Lưu mô hình và vectorizer
    model.save_model('model.pkl', 'vectorizer.pkl')

    print("Mô hình đã được huấn luyện và lưu thành công.")


if __name__ == "__main__":
    create_and_train_model()
