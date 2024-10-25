# app.py

import sys
from PyQt5 import QtWidgets
from gui import MainWindow
from database import Database


def main():
    app = QtWidgets.QApplication(sys.argv)
    db = Database('LAPTOP-2PTIGU9P\\SQLEXPRESS', 'PhishingDB')

    main_window = MainWindow(db)
    main_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
