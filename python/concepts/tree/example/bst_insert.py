'''
insert of a key:
         100                               100
        /   \        Insert 40            /    \
      20     500    --------->          20     500 
     /  \                              /  \  
    10   30                           10   30
                                              \   
                                              40

Reference:
    - https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
'''

class Node: 
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def insert(root, key):
    ''' insert a key into root. '''
    if root is None:
        return Node(key)
    
    if root.val == key:
        return root
    elif root.val > key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):    
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# def inorder_res(root):
#     result = []
    
#     queue = []
#     next_queue = []
    
#     while queue is not None:
#         result.append(root.val)
        
#         if root.right is not None:
#             next_queue.append(root.right)
#         if root.left is not None:
#             next_queue.append(root.left)
#         root = next_queue.pop()
        
#     return result


if __name__ == '__main__':
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
        
    #    50
    #  /     \
    # 30     70
    #  / \ / \
    # 20 40 60 80

    inorder(r)
    
    # print(inorder_res(r))
    