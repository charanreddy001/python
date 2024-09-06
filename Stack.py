from collections import deque
s = []
s.append("hello")
s.append("jillema jitta")
print(s)
s.pop()
print(s)
# this will remove last element and display that element
print(s[-1])
stack = deque()
print(dir(stack))
# this all are the methods in deque()
stack.append("inflammable Gitta")
stack.append("ni notla na modda")
print(stack)

# to better understand stack you need to see the picture in one note
# this type is " last in and first out "
# the last one which has gone inside will come out

class stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

s = stack()
s.push(90)

print(s.peek())


