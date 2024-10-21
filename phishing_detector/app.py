from gui import App
from train_model import create_and_train_model

if __name__ == "__main__":
    app = App()  # Tạo đối tượng App
    app.run()    # Chạy ứng dụng
    create_and_train_model()