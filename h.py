import numpy

arr1d = numpy.array([23, 34, 45, 56, 65, 78])
print(arr1d.shape)
print(arr1d.dtype)
print(arr1d.ndim)
print(arr1d.size)

# NUMPY means numerical python

arr2d = numpy.array([[234, 34, 6753, 436, 73], [432, 57, 768, 890, 43], [589, 5785, 34, 345, 353]])
print(arr2d)
print(arr2d.shape)
print(arr2d.ndim)
print(arr2d.size)
print(arr2d.dtype)

# to print elements in array by using for loop
for ele in arr2d:
    print(ele)

print('')
# multidimensional array
# in 3d array first number represents number of 2d boxes are present;( "2", 3, 3)
# then remaining two numbers represents that the matrix(box) is "3*3"
# see screenshots

# reshaping numpy array
arr = numpy.array([12, 23, 34, 4, 5, 67, 70, 23])
print(arr)
print(arr.shape)
print(arr.ndim)
print(" ")
# here this one is a one dimensional array with 8 elements
# now we are reshaping this one into a 3d array with (2,2,2)
# that mean there are two 2d array with 2*2 measurements

print(" ")
res = arr.reshape(2, 2, 2)
print(res)
print("dimensions: ", res.ndim)
# we have successfully turned 1D array into 3D array
