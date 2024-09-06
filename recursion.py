
def fact(n):
    if n == 1 or 0 :
        return 1
    else:
        return n * fact(n-1)

x = fact(5)
print(x)
# this is nothing but recursion we use same function inside that function
# we must prescribe a base condition until which has to be continued
