from PyQt5.QtWidgets import QMainWindow
from .ui_sudoku import Ui_MainWindow
from enum import Enum, auto
from Model.sudoku_model import SudokuModel
import requests


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

    # TODO Enum?
    BACKSPACE_KEY = '\b'
    DELETE_KEY = '\x7f'
    ZERO_KEY = '0'
    SELECTED_STYLE = "background-color: lightblue; border: 2px solid blue;"
    DEFAULT_STYLE = "background-color: white;"
    query = """{newboard(limit: 1) {grids {value, solution, difficulty}results,message}}"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = SudokuModel()

        self.selected_cell = None

        button_map = GenButtonMap()  #TODO?

        self.PB_LoadBoard.clicked.connect(self.load_board_from_api)
        self.PB_PrintBoard.clicked.connect(lambda: print(self.model))
        self.mousePressEvent = self.mouse_click_event

        for row in range(9):
            for col in range(9):
                cell_name = f"Cell_{row}{col}"
                cell = getattr(self, cell_name)
                cell.mousePressEvent = lambda event, _cell=cell: self.cell_clicked(_cell)

    def mouse_click_event(self, event):
        # Reset the selected cell to None if user clicks outside the cell grid
        if self.selected_cell:
            self.selected_cell.setStyleSheet(self.DEFAULT_STYLE)
        self.selected_cell = None

    def cell_clicked(self, cell):
        if self.selected_cell:
            self.selected_cell.setStyleSheet(self.DEFAULT_STYLE)
        self.selected_cell = cell
        self.selected_cell.setStyleSheet(self.SELECTED_STYLE)

    def keyPressEvent(self, event):
        if self.selected_cell:
            key = event.text()
            if key.isdigit() and 1 <= int(key) <= 9:
                self.selected_cell.setText(key)
                row, col = self.selected_cell.property('row'), self.selected_cell.property('col')
                self.model.set_number(row, col, int(key))
            elif key in (self.ZERO_KEY, self.BACKSPACE_KEY, self.DELETE_KEY):
                self.selected_cell.setText("")
                row, col = self.selected_cell.property('row'), self.selected_cell.property('col')
                self.model.set_number(row, col, 0)

    def load_api_view(self, sudoko_board):  #TODO decorator?
        for row in range(9):
            for col in range(9):
                cell_name = f"Cell_{row}{col}"
                cell = getattr(self, cell_name)
                if sudoko_board[row][col] == 0:
                    cell.setText("")
                else:
                    cell.setText(str(sudoko_board[row][col]))

    def load_board_from_api(self):
        query = '{newboard(limit:1){grids{value,solution,difficulty},results,message}}'
        url = f'https://sudoku-api.vercel.app/api/dosuku?query={query}'

        try:
            response = requests.get(url)
            data = response.json()

            if "newboard" in data and "grids" in data["newboard"] and len(data["newboard"]["grids"]) > 0:
                sudoku_data = data["newboard"]["grids"][0]
                self.model.load_api_data(sudoku_data["value"])
                self.load_api_view(sudoku_data["value"])
            else:
                print("No Sudoku data found in the response.")
        except requests.exceptions.ConnectionError as e:
            print("Error:", e)  #TODO inform the user with GUI window to try again


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