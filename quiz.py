# QLA from coding.py
text = "python is amazing"
print(text.find("c++"))
print(text.find("python"))
# if text is found it returns "0" else it will return "-1"
# in python -1 is considered as true in boolean while "0" is considered as false
if text.find("c++"):
    print("found c++")
else:
    print("C++ is not found")

a = 23
b = 435
c = 56
print(a, b, c, sep='@ ')
# it is used to separate things
print("1,2,3,4,4,674")


# to find number of divisible of a number
n=int(input("enter the number "))
count = 0
for i in range(1,n + 1):
    if n%i == 0:
        count += 1
print(count)


age = 2
if age >= 18 or ...:
    print("i can drive on my own")
