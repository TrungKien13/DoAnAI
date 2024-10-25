# phishing_model.py

from sklearn.tree import DecisionTreeClassifier
import pandas as pd

class PhishingModel:
    def __init__(self):
        self.model = DecisionTreeClassifier()

    def train(self, data):
        # Giả định rằng 'data' là DataFrame đã được chuẩn bị
        X = data.drop('label', axis=1)  # Tính năng
        y = data['label']                # Nhãn
        self.model.fit(X, y)

    def predict(self, features):
        return self.model.predict([features])
