'''
新增 NodeTree 的練習與測試

'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def set_right(self, n):
        self.right = n
        return self
        
    def set_left(self, n):
        self.left = n
        return self
    
    
if __name__ == '__main__':
    n5 = Node(5, None, None)
    n4 = Node(4, None, None)
    n2 = Node(2, n4, n5)
    n3 = Node(3, None, None)
    root = Node(1, n2, n3)
    
    print(root.val)
    print(root.left.val)
    print(root.right.val)
    
    print(root.left.left.val)
    print(root.left.right.val)
    
    
    node10 = Node(10)
    node11 = Node(11)
    node12 = Node(12)
    node10.set_left(node11) \
        .set_right(node12)
    
    print(node10.val)
    print(node10.left.val)
    print(node10.right.val)