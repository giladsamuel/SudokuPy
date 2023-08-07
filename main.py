# from View import custom_sudoku_ui
from View.custom_sudoku_ui import CustomMainWindow
from PyQt5.QtWidgets import QApplication


app = QApplication([])
window = CustomMainWindow()
window.show()
app.exec_()