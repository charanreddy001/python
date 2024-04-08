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
