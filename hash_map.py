# to get ascii value of a character we use the function ord()
# go to onenote > hash map concept "first learn all of that"


# there we for getting a particular value to map we get a number by ascii values

print(ord("a"))
# this is ascii value of that character
print("")


# function to get ascii for many characters is:
def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
        final = h % 100
    print(final)
# here we assume '100' as the size of list
# if we assume 10  size of list then it gives at which index it should be placed like "1"



get_hash('charan')
get_hash("charan 6")

class Hashtable:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
            return h % self.max

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

t = Hashtable()

t['march 1'] = 100
t['dec 17'] = 27
t['may 6'] = 39
t['may 7'] = 23

print(t.arr)


