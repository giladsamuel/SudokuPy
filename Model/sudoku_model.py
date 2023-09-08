from sudoku import Sudoku
from square_3x3 import Square3x3

class SudokuModel(Sudoku):
    def __init__(self, *args, **kwargs):
        super(SudokuModel, self).__init__(*args, **kwargs)

    def load_api_data(self, sudoko_data):
        sudoko_board = [[None] * 3 for _ in range(3)]
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                square_subarray = [sudoko_data[i][col:col+3] for i in range(row, row+3)]
                sub_row = row // 3
                sub_col = col // 3
                self.board[sub_row][sub_col] = Square3x3.from_2d_array(square_subarray)

    def __str__(self):
        rows = []
        for row in range(9):
            if row % 3 == 0 and row != 0:
                rows.append("-" * 21)

            row_string_from_squares = []

            for col in range(9):
                if col % 3 == 0 and col != 0:
                    row_string_from_squares.append("|")
                square = self.board[row // 3][col // 3]
                value = square.get_cell(row % 3, col % 3)
                row_string_from_squares.append(str(value))

            rows.append(" ".join(row_string_from_squares))

        return "\n".join(rows)



    # def set_number(self, row, col, number):
    #     square = self.board[row / 3][col / 3]
    #     square.set_xy(number)
    #
    # def get_number(self, row, col):
    #     square = self.board[row / 3][col / 3]
    #     return square.get_cell(row//3, col//3)