'''
basic list concept.
    - 先列出可能的操作
    
'''
arr = [1, 2, 5, 6, 11, 9] # 6 elements.


def get_object():
    for i in arr:
        print(i)
    
def use_range():
    # 使用 range, 數量(字), 需搭配 list 抓取值
    for i in range(len(arr)):
        print(arr[i]) # [1, 2, 5, 6, 11, 9]
        
    for i in range(0, len(arr), 1):
        print(i) # [0, 1, 2, 3, 4, 5, 6]
        
    for i in range(len(arr), 0, -1):
        print(i) # [5, 4, 3, 2, 1]
    
def use_while_loop():
    i = 0
    while i < len(arr):
        print(arr[i])
        i += 1


if __name__ == '__main__':
    # get_object()

    # use_range()
        
    use_while_loop()
    
    
    