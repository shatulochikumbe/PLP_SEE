# Last In First Out (LIFO) - Stack
stack = []


stack.append(10) #push
stack.append(20)
stack.append(30) 
stack.append(40)
stack.append(50)


stack.pop ()

# print(stack[0])
print(stack)

print(stack[-1])

# print(stack[-1]) #

# Stack (LIFO)


# First In First Out (FIFO) - Queue
# Queue (FIFO)

from collections import deque

queue = deque()

queue.append('A')
queue.append('B')
queue.append('C')
print(queue.popleft())
