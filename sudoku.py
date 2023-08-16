from square_3x3 import Square3x3


class Sudoku:
    def __init__(self):  # TODO inheritance and overriding
        self.board = [[Square3x3() for _ in range(3)] for _ in range(3)]

    @classmethod
    def from_board(cls, sudoko_board):
        sudoko_obj = cls()
        sudoko_obj.board = [[Square3x3.from_2d_array(sudoko_board[i][j]) for i in range(3)] for j in range(3)]
        return sudoko_obj

    def set_number(self, row, col, number):
        square = self.board[row // 3][col // 3]
        square.set_xy(row % 3, col % 3, number)

    def get_number(self, row, col):
        square = self.board[row / 3][col / 3]
        return square.get_cell(row//3, col//3)

    def is_valid(self) -> bool:  #TODO
        for i in range(3):
            for j in range(3):
                pass


# a = Sudoku()
# for row in a.board:
#     for obj in row:
#         print(obj) # print(Square3x3.__str__(obj))
# sqr = a.board[0][0]
# num = sqr.np_2d_array[0][0]
# print(num)