"""
bubble sorting algorithm.

1. 順序從右到左開始 或是 左到右開始
2. 從array[0] 開始到 array[n-1]，由於每次都會比較大小並對調。
3. 每次回合結束，都會確保最小的數值已經被放置最左邊。
"""


def bubble_sort(a: list):
    print(f'the origin array = {a}.')
    n = len(a)

    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


if __name__ == '__main__':
    arr = [2, 3, 1, 6, 9, 11, 5]
    res = bubble_sort(arr)
    print(f'after sorting, the result = {res}')