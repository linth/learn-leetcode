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
    

def preorder(root):
    # preorder: [root, left, right]
    if root is None:
        return []
    
    return [root.val] + preorder(root.left) + preorder(root.right)
    
def inorder(root):
    # inorder: [left, root, right]
    if root is None:
        return []
    
    return inorder(root.left) + [root.val] + inorder(root.right)

def postorder(root):
    # postorder: [left, right, root]
    if root is None:
        return []
    
    return postorder(root.left) + postorder(root.right) + [root.val]

def levelorder(root):
        
    queue, next_queue = [root], []
    level, result = [], []
    
    while queue != []:
        for i in queue:
            result.append(i.val)
            
            if i.left is not None:
                next_queue.append(i.left)
            if i.right is not None:
                next_queue.append(i.right)
        # result.append(level)
        level = []
        queue = next_queue
        next_queue = []
    return result

    
if __name__ == '__main__':
    n5 = Node(5, None, None)
    n4 = Node(4, None, None)
    n2 = Node(2, n4, n5)
    n3 = Node(3, None, None)
    root = Node(1, n2, n3)
    
    # print(root.val)
    # print(root.left.val)
    # print(root.right.val)
    
    # print(root.left.left.val)
    # print(root.left.right.val)
    
    
    node10 = Node(10)
    node11 = Node(11)
    node12 = Node(12)
    node13 = Node(13)
    node14 = Node(14)
    node10.set_left(node11) \
        .set_right(node12)
    node11.set_left(node13) \
        .set_right(node14)
    
    # print(node10.val)
    # print(node10.left.val)
    # print(node10.right.val)
    
    print('preorder: ', preorder(node10))
    print('inorder: ', inorder(node10))
    print('postorder: ', postorder(node10))
    
    print('postorder partial tree: ', postorder(node11)) # partial tree.
    print('levelorder: ', levelorder(node10))