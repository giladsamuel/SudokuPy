import numpy as np
from square_3x3 import Square3x3
import requests

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

# url = "https://sudoku-api.vercel.app/api/dosuku"
#
# response = requests.post(url, json={'query': query})
#
# # somethong = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]] for _ in range(3)]
# print(response)
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