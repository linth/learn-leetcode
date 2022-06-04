'''
Binary Search Tree | Set 1 (Search and Insertion)
    - search a node in BST.
    - 任一個節點的左子樹都比父節點小，右子樹都比父節點大
    - 且每一個節點的值都不重複。
    
Reference:
    - https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search(root, key):
    ''' find a node with key value. '''
    if root is None or root.val == key:
        return root
    
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)


if __name__ == '__main__':
    node3 = Node(3, Node(1, None, None), Node(6, Node(4, None, None), Node(7, None, None)))
    
    root = Node(8, node3, Node(10, None, Node(14, Node(13, None, None), None)))
    
    # res = search(root, 10) # find node 10.
    res = search(root, 6) # find node 6.
    # res = search(root, 14) # find node 14.
    
    if res.val != None:
        print('val', res.val)
    if res.left != None:
        print('left val', res.left.val)
    if res.right != None:
        print('right val', res.right.val)
    
    print(root) # <__main__.Node object at 0x000002C0AF77AC40>
    