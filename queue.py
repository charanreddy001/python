
# implementation of queue using list in python

stock_prices =[]
stock_prices.insert(0,132.2)
stock_prices.insert(0,135.1)
stock_prices.insert(0,150.09)
# here we are continuously inserting elements at zero("0") index
# after indexing elements that way newly inserted element will just be at first place then previous element will be pushed next
print(stock_prices.pop())
# this will be implemented just as we are expected like QUEUE

# first inserted element will be removed first


#  but implementing using list is not good

# so we use queue from collection

from collections import deque
q = deque()

q.appendleft(90)
q.appendleft(70)
q.appendleft(30)
q.appendleft(20)

print(q.pop())


from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()  # Initialize deque

    def enqueue(self, val):
        self.buffer.appendleft(val)  # Add to the front of the deque

    def dequeue(self):
        return self.buffer.pop()  # Remove from the back of the deque

    def is_empty(self):
        return len(self.buffer) == 0  # Check if the deque is empty

    def size(self):
        return len(self.buffer)  # Return the size of the deque


q = Queue()
q.enqueue({'company': 'walmart', 'time': '10:30:12', 'price': 100})
q.enqueue({'company': 'walmart', 'time': '10:31:12', 'price': 100.2})
q.enqueue({'company': 'walmart', 'time': '10:31:12', 'price': 100.22})
q.enqueue({'company': 'walmart', 'time': '10:31:12', 'price': 101.2})

print(q.buffer)  # Print the deque directly
print(q.dequeue())
# this gives the first element entered 


