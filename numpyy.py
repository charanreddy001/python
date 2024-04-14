import numpy as np

my_list = [[10, 20, 30, 40], [60, 70, 80, 90], [23, 45, 565, 65]]
matrix = np.array(my_list)
print(matrix)
print()
# for slicing
# [row_lwr : row_upp , col_low : col_upp]
# here lower limit is the original number but upper limit is +1 to original index number
resultant = matrix[1:2, 1:4]
print(resultant)
print()
# here we need numbers printed to be started from row 1 and end at row 3 same as column also
# and here numbering starts from "0" this thing is main to remember
exmp1 = matrix[0:2, 0:2]
print(exmp1)
print()

exmp2 = matrix[1:4, 1:2]
print(exmp2)
print()

exmp3 = matrix[0:3, 1:3]
print(exmp3)

# creating one dimensional array
# if here datatype is not given default data type is float
n = int(input("enter size: "))
arr = np.ndarray(shape=(n), dtype=int)

print(f"enter {n} elements: ")
for i in range(n):
    arr[i] = int(input())

print("array elements :", arr)

# creating second dimensional array
row = int(input("enter row size: "))
col = int(input("enter column size: "))
matrixx = np.ndarray(shape=(row, col), dtype=int)
print("size: ", matrixx.size)
print("shape: ", matrixx.shape)
print('dimensions: ', matrixx.ndim)


print("hello")
# creating ndimensional array
arr = np.ndarray(shape=5, dtype=int)
n = arr.size
print("enter %d elements: " %n)
for i in range(n):
    arr[i] = int(input())
print("elements: ", arr)

rows = int(input("enter number of rows: "))
column = int(input("enter number of columns: "))

creating = np.ndarray(shape=(rows, column), dtype=int)
print(f"enter {rows*column} elements of {rows}*{column} matrix: ")
for rows in range(rows):
    for column in range(column):
        creating[rows][column] = int(input())
print(f"{rows}*{column} matrix is : ")
print(creating)
