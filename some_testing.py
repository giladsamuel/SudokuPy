import numpy as np
from square_3x3 import Square3x3
# import requests
# Create a 9x9 2D array (list of lists)
big_array = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 5, 6, 7, 8, 9, 1, 2, 3],
    [3, 5, 6, 7, 8, 9, 1, 2, 3],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [5, 5, 6, 7, 8, 9, 1, 2, 3],
    [6, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 5, 6, 7, 8, 9, 1, 2, 3],
    [8, 5, 6, 7, 8, 9, 1, 2, 3],
    [9, 8, 9, 1, 2, 3, 4, 5, 6]
]

# Initialize a list to store the 3x3 subarrays
subarrays = []

# Iterate over rows of the big array with step size 3
for row in range(0, 9, 3):
    # Iterate over columns of the big array with step size 3
    for col in range(0, 9, 3):
        # Create a 3x3 subarray by slicing the big array
        subarray = [big_array[i][col:col+3] for i in range(row, row+3)]
        subarrays.append(subarray)

# Print the subarrays
for subarray in subarrays:
    for row in subarray:
        print(row)
    print()

#
# def load_sudoku_board(difficulty="Hard"):
#     query = f"""
#     {{
#       newboard(limit: 1) {{
#         grids {{
#           value
#           solution
#           difficulty
#         }}
#       }}
#     }}
#     """
#     url = "https://sudoku-api.vercel.app/api/dosuku?query=" + query
#
#     # try:
#     print(query)
#     response = requests.get(url)
#     print(response)
#     data = response.json()
#     print(data)
#     if "newboard" in data and "grids" in data["newboard"] and len(data["newboard"]["grids"]) > 0:
#         sudoku_data = data["newboard"]["grids"][0]
#         print("type", type(sudoku_data["value"]))
#         return sudoku_data
#     else:
#         print("No Sudoku data found in the response.")
#         return None
#     # except Exception as e:
#     #     print("Error:", e)
#     #     return None
#
#
# # Example usage
# if __name__ == "__main__":
#     sudoku_data = load_sudoku_board()
#     if sudoku_data:
#         print("Sudoku Value:\n", sudoku_data["value"])
#         print("Sudoku Solution:\n", sudoku_data["solution"])
#         print("Sudoku Difficulty:", sudoku_data["difficulty"])
#
# # def load_sudoku_board():
# #     url = "https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value,solution,difficulty},results,message}}"
# #
# #     try:
#         response = requests.get(url)
#         data = response.json()
#
#         if "newboard" in data and "grids" in data["newboard"] and len(data["newboard"]["grids"]) > 0:
#             sudoku_data = data["newboard"]["grids"][0]
#             return sudoku_data
#         else:
#             print("No Sudoku data found in the response.")
#             return None
#     except Exception as e:
#         print("Error:", e)
#         return None
# if __name__ == "__main__":
#     sudoku_data = load_sudoku_board()
#     if sudoku_data:
#         print("Sudoku Value:\n", sudoku_data["value"])
#         print("Sudoku Solution:\n", sudoku_data["solution"])
#         print("Sudoku Difficulty:", sudoku_data["difficulty"])
# query = ""
#
# url = "https://sudoku-api.vercel.app/api/dosuku"
# #
# response = requests.post(url, json={'query': query})
# #
# # # somethong = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]] for _ in range(3)]
# # print(response)
# print(response.json())
# arr1 = np.array([1, 2, 3])
# arr2 = arr1.copy()
#
# arr2[0] = 10
#
# print(arr1)  # Output: [1, 2, 3]
# print(arr2)  # Output: [10, 2, 3]
#
# list1 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# square1 = Square3x3.from_2d_array(list1)
#
# list2 = [[1, 2, 3], [4, 5, 9], [6, 7, 8]]
#
#
# square2 = Square3x3.from_2d_array(list2)
# print(square1.np_2d_array)
# print(square1)
# print(square1.get_cell(8, 9))
# print(repr(str(square1)))
#
# print(square1.all_there())
# print(square2.all_there())