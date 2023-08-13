from __future__ import annotations
import numpy as np


class Square3x3:
    """
    A class representing a 3x3 square with numpy array in the Sudoku game.
    """

    def_size = 3
    def_val = 0
    err_val = -1

    def __init__(self) -> None:

        self.np_2d_array = np.full((self.def_size, self.def_size), self.def_val)

    @classmethod
    def from_2d_array(cls, array_2d) -> Square3x3:
        """
        Constructs a Square3x3 object whose values are taken from a 2D array.
        If the given array’s size is bigger than 3X3, only the first 3X3 cells are taken.
        If the given array is smaller, the rest of the cells are initialized to –1.
        The given array can non-symmetrical.

        :param array_2d: (list[list]) A 2D array of values.
        :returns: Square3x3: A Square3x3 object with the values from the given 2D array.
        """
        square = cls()

        for i in range(min(Square3x3.def_size, len(array_2d))):
            for j in range(min(Square3x3.def_size, len(array_2d[i]))):
                square.np_2d_array[i][j] = array_2d[i][j]

        return square

    @classmethod
    def from_other_square(cls, other_square: Square3x3) -> Square3x3:
        """
        Copy constructor.
        Constructs a Square3x3 object whose values are taken from other Square3x3 object

        :param other_square: Square3x3 object
        """
        if not isinstance(other_square, Square3x3):
            raise TypeError("other_square must be Square3x3 object.")

        square = cls()
        square.np_2d_array = other_square.np_2d_array.copy()

        return square

    def get_cell(self, row: int, col: int) -> int:
        """
        Returns the value in the (row, col) cell.
        If the row and/or col are out of the array bounds, returns –1.
        Legal values for row/col are 0,1,2.

        :param row: The cell's row
        :param col: The cell's column
        """
        if -1 < row < self.def_size and -1 < col < self.def_size:
            return self.np_2d_array[row][col]
        raise IndexError
        return self.err_vall

    def set_xy(self, row: int, col: int, value: int):
        """
        Sets the cell (row, col) in the array to the given value.
        If the row and/or col are out of the array bounds – does nothing.
        Legal values for row/col are 0,1,2.

        :param row: The row of the cell to be set.
        :param col: The column of the cell to be set.
        :param value: The value of the cell to be set to.
        """
        if -1 < row < self.def_size and -1 < col < self.def_size:
            self.np_2d_array[row][col] = value

    def __str__(self) -> str:
        """
        Returns a String representation of the array.

        :return: The square as a string
        """
        string = str()

        for i in range(self.def_size):
            string = f'{string}{self.np_2d_array[i][0]}'  # solve fence post problem

            for j in range(1, self.def_size):
                string = f'{string}\t{self.np_2d_array[i][j]}'

            string = f'{string}\n'

        return string

    def all_there(self) -> bool:
        """
        Check if all integers 1-9 are in the given square.

        :return: True - if all integers 1-9 are in the given square, false - otherwise.
        """
        for num in range(1, 10):
            if not np.any(self.np_2d_array == num):
                return False

        return True

    def whos_there_row(self, row: int, values: list):
        """
        Initialize true in the matching 'values' array cell
        For each integer between 1-9 which appear in the given row.

        :param row: The row to take the integers from.
        :param values: The boolean array to initialize true in its cells if needed.
        """
        if row < 0 or row > 2 or values is None:
            return
        if len(values) != 10:
            return
        for col in range(3):
            if self.check_good_num(row, col):
                values[self.np_2d_array[row][col]] = True

    def whos_there_col(self, col: int, values: list):
        """
        Initialize true in the matching 'values' array cell
        For each integer between 1-9 which appear in the given column.

        :param col: The column to take the integers from.
        :param values: The boolean array to initialize true in its cells if needed.
        """
        if col < 0 or col > 2 or values is None:
            return
        if len(values) != 10:
            return
        for row in range(3):
            if self.check_good_num(row, col):
                values[self.np_2d_array[row][col]] = True

    def check_good_num(self, row, col) -> bool:
        """
        check if the integer in the given row and column is between 1-9

        :return: True - if it is, False otherwise.
        """
        return 1 <= self.np_2d_array[row][col] <= 9
