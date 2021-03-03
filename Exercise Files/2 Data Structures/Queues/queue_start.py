# try out the Python stack functions
from collections import deque

# TODO: create a new empty stack
queue = deque()

# TODO: push items onto the stack
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# TODO: print the stack contents
print(queue)

# TODO: pop an item off the stack
x = queue.popleft()
print(queue)