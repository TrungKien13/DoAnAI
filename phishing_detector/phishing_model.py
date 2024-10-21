import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer

class PhishingModel:
    def __init__(self):
        self.model = None
        self.vectorizer = None

    def train(self, contents, labels):
        """Huấn luyện mô hình với dữ liệu đầu vào."""
        self.vectorizer = CountVectorizer()
        X = self.vectorizer.fit_transform(contents)
        y = labels

        # Huấn luyện mô hình
        self.model = DecisionTreeClassifier()
        self.model.fit(X, y)

    def save_model(self, model_file, vectorizer_file):
        """Lưu mô hình và vectorizer vào file."""
        with open(model_file, 'wb') as f:
            pickle.dump(self.model, f)
        with open(vectorizer_file, 'wb') as f:
            pickle.dump(self.vectorizer, f)

    def load_model(self, model_path, vectorizer_path):
        with open(model_path, 'rb') as f:
            self.model, self.vectorizer = pickle.load(f)  # Tách mô hình và vectorizer

    def predict(self, url):
        X = self.vectorizer.transform([url])  # Biến đổi URL bằng vectorizer
        return self.model.predict(X)[0]  # 0 cho an toàn, 1 cho độc hại
