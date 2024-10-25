from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from database import DatabaseConnection

def preprocess_data(data):
    # Chuyển đổi dữ liệu URL và email về vector số học
    return np.array([list(map(int, row[0])) for row in data])

def create_and_train_model():
    db = DatabaseConnection(server='LAPTOP-2PTIGU9P\\SQLEXPRESS', database='PhishingDB')

    # Lấy dữ liệu từ bảng CLEAN_URL và Emails
    urls_data = db.fetch_data("SELECT Vector FROM URLTokensVectors WHERE Label IS NOT NULL")
    urls_labels = [row[1] for row in db.fetch_data("SELECT Label FROM URLTokensVectors WHERE Label IS NOT NULL")]

    emails_data = db.fetch_data("SELECT EmailContent FROM Emails WHERE Email_laybers IS NOT NULL")
    emails_labels = [row[2] for row in db.fetch_data("SELECT Email_laybers FROM Emails WHERE Email_laybers IS NOT NULL")]

    # Kiểm tra dữ liệu
    print(f"URLs Data: {urls_data}")
    print(f"URLs Labels: {urls_labels}")
    print(f"Emails Data: {emails_data}")
    print(f"Emails Labels: {emails_labels}")

    # Kiểm tra nếu dữ liệu rỗng
    if not urls_data or not urls_labels or not emails_data or not emails_labels:
        print("Lỗi: Dữ liệu URL hoặc Email trống.")
        db.close()
        return None

    # Tiền xử lý và chuẩn bị dữ liệu
    X_urls = preprocess_data(urls_data)
    y_urls = np.array(urls_labels)
    X_emails = preprocess_data(emails_data)
    y_emails = np.array(emails_labels)

    # Kết hợp dữ liệu URL và email để tạo mô hình
    X_combined = np.vstack((X_urls, X_emails))
    y_combined = np.hstack((y_urls, y_emails))

    # Tạo mô hình và huấn luyện với dữ liệu
    model = DecisionTreeClassifier()
    X_train, X_test, y_train, y_test = train_test_split(X_combined, y_combined, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, predictions)}")

    db.close()
    return model
