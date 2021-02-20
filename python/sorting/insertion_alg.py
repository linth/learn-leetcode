"""
insertion sorting algorithm.

1. 順序從左到右開始
2. 從剩下的array, 找出最小的數值
3. 取最小值進行替換
"""

def insertion_sort(a: list):
    print(f'the origin array = {a}.')

    n = len(a)

    for i in range(1, n):
        key = a[i]
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a


if __name__ == '__main__':
    arr = [2, 3, 1, 61, 9, 11, 5]
    res = insertion_sort(arr)
    print(f'after sorting, the result = {res}')