from sudoku import Sudoku

class SudokuModel(Sudoku):
    def __init__(self, *args, **kwargs):
        super(SudokuModel, self).__init__(*args, **kwargs)

    # def set_number(self, row, col, number):
    #     square = self.board[row / 3][col / 3]
    #     square.set_xy(number)
    #
    # def get_number(self, row, col):
    #     square = self.board[row / 3][col / 3]
    #     return square.get_cell(row//3, col//3)