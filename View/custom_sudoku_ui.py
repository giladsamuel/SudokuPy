from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from .ui_sudoku import Ui_MainWindow
from enum import Enum, auto

class Cmds(Enum):
    NUM = auto()
    DEL = auto()
    MOUSE = auto()
    CELLCLICK = auto()
    LOAD = auto()
    RESTART = auto()
    SOLVE = auto()
    CLEAR = auto()


def GenButtonMap():
    return {Cmds.LOAD: 'Load a new Board',
              Cmds.RESTART: 'Restart',
              Cmds.SOLVE: 'Solve',
              Cmds.CLEAR: "Clear"}

class CustomMainWindow(QMainWindow, Ui_MainWindow):



    def __init__(self):
        super().__init__()
        self.setupUi(self)
        button_map = GenButtonMap()

        for row in range(1, 10):
            for col in range(1, 10):
                button_name = f"PB_{row}{col}"
                button = getattr(self, button_name)
                button.clicked.connect(lambda checked, button=button: self.cell_clicked(button))


    def cell_clicked(self, button):
        # TODO focus bug when i minimize the window and return it
        # TODO Enum?
        BACKSPACE_KEY = '\b'
        DELETE_KEY = '\x7f'
        ZERO_KEY = '0'
        FOCUSED_STYLE = "background-color: lightblue;"
        DEFAULT_STYLE = ""

        def key_pressed(button, event):
            key = event.text()
            if key.isdigit() and 1 <= int(key) <= 9:
                button.setText(key)
                # Add your logic to update the underlying data structure for Sudoku
            elif key in (ZERO_KEY, BACKSPACE_KEY, DELETE_KEY):
                button.setText("")

        def set_focus(button):
            button.setDown(True)
            button.setStyleSheet(FOCUSED_STYLE)

        def clear_focus(button):
            button.setDown(False)
            button.setStyleSheet(DEFAULT_STYLE)

        set_focus(button)
        button.focusOutEvent = lambda event, button=button: clear_focus(button)
        button.keyPressEvent = lambda event, button=button: key_pressed(button, event)






    #     # Maps to map commands, keys and functions
    #     self.key_table = {k: Cmds.NUM for k in range(QtCore.Qt.Key_0, QtCore.Qt.Key_9+1)}
    #     self.key_table.update({QtCore.Qt.Key_Backspace: Cmds.DEL})
    #     self.func_map = {}
    #
    #     # Variables (UI)
    #     self.cells = self.CreateBoard(self)
    #
    # def cell_clicked(self, row, col):
    #     def key_pressed(event):
    #         key = event.text()
    #         if key.isdigit() and 1 <= int(key) <= 9:
    #             # Update the button's text and handle your Sudoku logic
    #             button = getattr(self, f"PB_{row}{col}")
    #             button.setText(key)
    #             # Add your logic to update the underlying data structure for Sudoku
    #
    #     button = getattr(self, f"PB_{row}{col}")
    #     button.setFocus()  # Make sure the button has focus
    #     button.keyPressEvent = key_pressed
    #
    # @staticmethod
    # def CreateBlock(parent, layout, bi, bj):
    #     block = Block(parent)
    #     layout.addWidget(block, bi, bj)
    #     return block
    #
    # @staticmethod
    # def CreateCell(i, j, boxes, click_func):
    #     bi, bj = i // 3, j // 3
    #     parent_box = boxes[bi][bj]
    #     cell = Cell(parent_box, i, j)
    #     cell.ConnectCelltoWindow(click_func)
    #     parent_box.AddCell(cell, i - 3*bi, j - 3*bj)
    #     return cell
    #
    # def CreateBoard(self, parent, layout):
    #     """ Creates board display with initial board values and candidates """
    #     # Create boxes for each 9x9 block
    #     blocks = [[self.CreateBlock(parent, layout, bi, bj) for bj in range(3)] for bi in range(3)]
    #     return [[self.CreateCell(i, j, blocks, self.CellClicked) for j in range(9)] for i in range(9)]
    #
    #