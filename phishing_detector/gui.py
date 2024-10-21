import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, Menu, scrolledtext
from database import Database
from url_checker import URLChecker

class App:
    def __init__(self):  # Thay đổi object thành None
        self.root = tk.Tk()  # Khởi tạo cửa sổ chính
        self.root.title("Công Cụ Phát Hiện Lừa Đảo")
        self.root.geometry("600x400")
        self.url_checker = URLChecker()

        # Khởi tạo cơ sở dữ liệu
        self.db = Database()  # Chỉ cần tên server

        # Menu
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.options_menu = Menu(self.menu)
        self.menu.add_cascade(label="Tùy chọn", menu=self.options_menu)
        self.options_menu.add_command(label="Lịch sử", command=self.show_history)
        self.options_menu.add_separator()
        self.options_menu.add_command(label="Thoát", command=self.root.quit)

        # Giao diện chính
        self.label = tk.Label(self.root, text="Nhập Email hoặc URL:")
        self.label.pack()

        self.text_area = scrolledtext.ScrolledText(self.root, width=60, height=10)
        self.text_area.pack()

        self.check_button = tk.Button(self.root, text="Kiểm tra", command=self.check_input)
        self.check_button.pack()

    def check_input(self):
        content = self.text_area.get("1.0", tk.END).strip()
        if content:
            if content.startswith("http"):
                result = self.url_checker.check_url(content)
                messagebox.showinfo("Kết quả kiểm tra URL", result)
                self.db.insert_url(content, result)  # Lưu kết quả vào DB
            else:
                result = self.check_email(content)
                messagebox.showinfo("Kết quả kiểm tra Email", result)
            self.text_area.delete('1.0', tk.END)  # Xóa sau khi kiểm tra


    def check_email(self, email_content):
        """Kiểm tra nội dung email."""
        if "danger" in email_content:
            result = "Có thể nguy hiểm!"
            messagebox.showinfo("Kết quả kiểm tra Email", result)
            self.db.insert_email(email_content, result)  # Lưu email vào DB
            self.db.insert_history("Email", email_content, result)  # Lưu lịch sử
        else:
            result = "Có vẻ an toàn!"
            messagebox.showinfo("Kết quả kiểm tra Email", result)
            self.db.insert_email(email_content, result)  # Lưu email vào DB
            self.db.insert_history("Email", email_content, result)  # Lưu lịch sử

        # Kiểm tra URL trong email
        urls = self.extract_urls(email_content)
        if urls:
            url_response = messagebox.askyesno("Phát hiện URL",
                                               f"Email chứa URL: {', '.join(urls)}. Bạn có muốn kiểm tra không?")
            if url_response:
                for url in urls:
                    result = URLChecker(url)
                    messagebox.showinfo("Kết quả kiểm tra URL", f"URL: {url} - Kết quả: {result}")
                    self.db.insert_url(url, result)  # Lưu kết quả URL vào DB
                    self.db.insert_history("URL", url, result)  # Lưu lịch sử

    def extract_urls(self, email_content):
        """Trả về danh sách các URL trong nội dung email."""
        # Giả lập việc trích xuất URL (thay đổi theo logic của bạn)
        return [url for url in email_content.split() if url.startswith("http")]

    def show_history(self):
        """Hiển thị lịch sử kiểm tra dưới dạng bảng."""
        history_records = self.db.fetch_history()

        # Tạo một cửa sổ mới để hiển thị lịch sử
        history_window = tk.Toplevel(self.root)
        history_window.title("Lịch sử Kiểm tra")

        # Tạo một Treeview để hiển thị lịch sử
        tree = ttk.Treeview(history_window, columns=("Type", "Content", "Result", "Timestamp"), show='headings')
        tree.heading("Type", text="Loại")
        tree.heading("Content", text="Nội dung")
        tree.heading("Result", text="Kết quả")
        tree.heading("Timestamp", text="Ngày")

        # Đặt độ rộng cho các cột
        tree.column("Type", width=100)
        tree.column("Content", width=300)
        tree.column("Result", width=150)
        tree.column("Timestamp", width=150)

        # Thêm dữ liệu vào Treeview
        for record in history_records:
            tree.insert("", tk.END, values=(record.Type, record.Content, record.Result, record.Timestamp))

        # Đặt Treeview vào cửa sổ
        tree.pack(expand=True, fill='both')

        # Cuộn thanh nếu có nhiều dữ liệu
        scrollbar = ttk.Scrollbar(history_window, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

        # Cài đặt kích thước cho cửa sổ
        history_window.geometry("600x600")
    def run(self):
        """Chạy ứng dụng."""
        self.root.mainloop()

