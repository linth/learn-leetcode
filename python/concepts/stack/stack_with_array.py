"""
Stack implementation with array.

- list
- queue
- linked list

Reference:
    - https://www.geeksforgeeks.org/stack-in-python/
"""
from queue import LifoQueue


s = []

s.append('a')
s.append('b')
s.append('c')

print('stack: ', s)

s.pop()
print('stack: ', s)

# =============================================
# METHOD 1: using queue to implement the stack.
# =============================================
stack = LifoQueue(maxsize=3)
print('the qsize: ', stack.qsize()) # 0

stack.put(1)
stack.put(3)
stack.put(14)
# stack.put(5) # over 3 something error happened.
print('the qsize: ', stack.qsize(), stack.maxsize)

# check the stack is empty or not.
print(stack.empty())

res = stack.get() # get the last element.
print('the last element: ', res)


a = []
a.append(1)
a.append(2)
a.append(6)
print(a)
a.pop()
print(a)