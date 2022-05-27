"""
Queue implementation with Array.

The method of implementation:
    - list
    - collections.deque
    - queue.Queue

Reference:
    - https://www.geeksforgeeks.org/queue-in-python/
"""


if __name__ == '__main__':
    queue = []

    queue.append(1)
    queue.append(3)
    queue.append(7)
    queue.append(11)
    queue.append(25)

    print(f'the queue = {queue}')

    # delete the last element.
    queue.pop()
    print(f'the queue = {queue}')

    queue.pop(1)
    print(f'the queue = {queue}')

    # delete the first element.
    front_num = queue.pop(0)
    print(f'the queue = {queue}')
    print(front_num)
    