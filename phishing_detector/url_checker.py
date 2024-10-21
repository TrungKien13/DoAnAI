from phishing_model import PhishingModel

class URLChecker:
    def __init__(self):
        self.model = PhishingModel()
        self.model.load_model('model.pkl', 'vectorizer.pkl')  # Tải mô hình đã huấn luyện

    def check_url(self, url):
        """Kiểm tra URL có an toàn hay không."""
        prediction = self.model.predict(url)
        return "URL an toàn!" if prediction == 0 else "URL có thể độc hại!"
