"""
heap sorting algorithm.

https://www.geeksforgeeks.org/python-program-for-heap-sort/
"""

def heap_sort(a: list):
    print(f'the origin array = {a}.')
    return a


if __name__ == '__main__':
    arr = []
    res = heap_sort(arr)
    print(f'after sorting, the result = {res}')