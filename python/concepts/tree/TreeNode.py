
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

list_preorder, list_inorder, list_postorder = [], [], []

def preorder(root):
    if root:
        list_preorder.append(root.val) # print(root.val)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        list_inorder.append(root.val) # print(root.val)
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        list_postorder.append(root.val) # print(root.val),

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # preorder
    print('Preorder traversal of binary tree is: ')
    preorder(root)
    print(list_preorder)

    # inorder
    inorder(root)
    print(list_inorder)

    # postorder
    postorder(root)
    print(list_postorder)
    
        