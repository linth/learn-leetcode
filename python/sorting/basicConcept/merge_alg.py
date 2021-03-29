"""
merge sorting algorithm.

https://www.geeksforgeeks.org/python-program-for-merge-sort/
"""

def merge_sort(a: list):
    print(f'the origin array = {a}.')
    return a


if __name__ == '__main__':
    arr = []
    res = merge_sort(arr)
    print(f'after sorting, the result = {res}')