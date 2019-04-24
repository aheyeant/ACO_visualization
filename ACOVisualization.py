import sys

from PyQt5.QtWidgets import QApplication

from src.GUI import GUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())
