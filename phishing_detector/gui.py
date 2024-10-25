# gui.py

from PyQt5 import QtWidgets
from email_checker import EmailChecker
from url_checker import URLChecker

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setWindowTitle("Phishing Detection Tool")

        # Widgets
        self.email_input = QtWidgets.QLineEdit(self)
        self.url_input = QtWidgets.QLineEdit(self)
        self.check_email_button = QtWidgets.QPushButton("Check Email", self)
        self.check_url_button = QtWidgets.QPushButton("Check URL", self)

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("Enter Email:"))
        layout.addWidget(self.email_input)
        layout.addWidget(self.check_email_button)
        layout.addWidget(QtWidgets.QLabel("Enter URL:"))
        layout.addWidget(self.url_input)
        layout.addWidget(self.check_url_button)

        container = QtWidgets.QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Connect buttons to functions
        self.check_email_button.clicked.connect(self.check_email)
        self.check_url_button.clicked.connect(self.check_url)

    def check_email(self):
        email = self.email_input.text()
        checker = EmailChecker(self.db)
        try:
            result = checker.check(email)
            QtWidgets.QMessageBox.information(self, "Email Check Result", result)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def check_url(self):
        url = self.url_input.text()
        checker = URLChecker(self.db)
        try:
            result = checker.check(url)
            QtWidgets.QMessageBox.information(self, "URL Check Result", result)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

