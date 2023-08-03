from square_3x3 import Square3x3


class Sudoko:
    def __init__(self):
        self.board = [[Square3x3() for _ in range(3)] for _ in range(3)]

    @classmethod
    def form_board(cls, sudoko_board):
        sudoko_obj = cls()
        sudoko_obj.board = [[Square3x3.from_2d_array(sudoko_board[i][j]) for i in range(3)] for j in range(3)]
        return sudoko_obj

    def is_valid(self) -> bool:
        for i in range(3):
            for j in range(3):


a = Sudoko()
for row in a.board:
    for obj in row:
        print(obj) # print(Square3x3.__str__(obj))
# sqr = a.board[0][0]
# num = sqr.np_2d_array[0][0]
# print(num)