"""
selection sorting algorithm.

1. 順序從左到右開始
2. 從剩下的array, 找出最小的數值
3. 取最小值進行替換
"""

def selection_sort(a: list):
    print(f'the origin array = {a}.')

    n = len(a)

    for i in range(n):
        # find the minimum element in the ramaining unsorted array.
        min_index = i
        for j in range(i+1, n):
            if a[min_index] > a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a


if __name__ == '__main__':
    arr = [2, 3, 1, 6, 9, 11, 5]
    res = selection_sort(arr)
    print(f'after sorting, the result = {res}')