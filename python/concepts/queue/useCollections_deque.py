
from collections import deque
from queue import Queue

"""
collections' deque

感覺似乎可以看看就好，有太多種類可以使用。大體挑選幾種常用的即可。

Reference:
    - https://www.geeksforgeeks.org/queue-in-python/?ref=lbp
"""

def use_queue():
    q = Queue(maxsize=5)

    q.put(1)
    q.put(5)
    q.put(6)
    q.put(11)
    q.put(20)

    print(f'{q}')
    print(q.get()) # 1
    print(q.get()) # 5
    print(q.get()) # 6
    print(q.get()) # 11
    print(q.get()) # 20
    print(q)
    print(q.empty())


def use_collections_deque():
    # 可直接使用現成的 collections: deque

    q = deque()

    q.append('a')
    q.append('b')
    q.append('c')

    print(q, type(q)) # deque(['a', 'b', 'c'])

    print(q.popleft()) # a
    print(q) # deque(['b', 'c'])

    print(q.pop()) # c
    print(q) # deque(['b'])


if __name__ == '__main__':
    # use Queue().
    use_queue()

    # use collections: deque.
    use_collections_deque()
