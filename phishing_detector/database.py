# database.py

import pyodbc


class Database:
    def __init__(self, server, database):
        self.connection = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
        self.cursor = self.connection.cursor()

    def fetch_emails(self):
        self.cursor.execute("SELECT * FROM Emails")
        return self.cursor.fetchall()

    def fetch_urls(self):
        self.cursor.execute("SELECT * FROM URLs")
        return self.cursor.fetchall()

    def log_history(self, type, content, result):
        self.cursor.execute("INSERT INTO history (type, content, result, timestamp) VALUES (?, ?, ?, GETDATE())",
                            (type, content, result))
        self.connection.commit()
