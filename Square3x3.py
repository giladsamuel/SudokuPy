import numpy as np

class Square3x3:
    
    def __init__(self, array=None):
        if(array is not None):
            if(array.shape == (3,3)):
                self.square = np.copy(array)
            else:
                self.square = np.array([[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]])
                if(array.shape[1]<3):
                    a=array.shape[1]
                else: a=3

                if(array.shape[0]<3):
                    b=array.shape[0]
                else: b=3

                for i in range(b):
                    for j in range(a):
                        self.square[i][j] =  array[i][j]

        else: #"Default Constructor""
            print("Default Constructor")
            self.square = np.array([[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]])

    def getCell(self, col: int, row: int):
        return self.square[col][row]

    def setXY(self, row: int,col: int,value: int):
        if row<0 or row>2 or col<0 or col>2:
            return
        else: self.square[row][col] = value

    def toString(self):
        string=""
        for i in range(3):
            for j in range(3):
                string += str(self.getCell(i,j)) + "\t"
            string += "\n"
        return string



c  = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,13],[13,14,15,16]])
print(c)
obj0 = Square3x3(c)
print(obj0.square)
obj1 = Square3x3()
print(obj1.square)
a= obj0.getCell(1,2)
print(a)
a= obj0.getCell(2,1)
print(a)
print(obj0.toString())