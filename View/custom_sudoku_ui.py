from PyQt5.QtWidgets import QMainWindow
from .sudoku_ui import Ui_MainWindow

class CustomMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        