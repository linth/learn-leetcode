'''
歸納四種 binary tree 的 traversal:
    - pre-order
    - in-order
    - post-order
    - level-order

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
        

class Solution:
    def preorderTraversal(self, root):
        # [root, left, right]
        if root is None:
            return []
        
        stack = [root]
        result = []
        
        while stack != []:
            root = stack.pop() # 因為使用pop, 所以要注意下面 root.right, root.left 順序
            result.append(root.val)
            
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return result
    
    def inorderTraversal(self, root):
        # [left, root, right]
        stack = [] # put root: TreeNode into this list.
        result = [] # final result.
        
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result    
    
    def postorderTraversal(self, root):
        # [left, right, root]
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return result[::-1]
    
    def levelorderTraversal(self, root):
        if root is None:
            return []
        
        queue, next_queue = [root], []
        level, result = [], []
        
        while queue != []:
            for item in queue:
                result.append(item.val)
                
                if item.left is not None:
                    next_queue.append(item.left)
                if item.right is not None:
                    next_queue.append(item.right)
                
            queue = next_queue
            next_queue = []
        return result


if __name__ == '__main__':
    
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    
    node1.set_left(node2).set_right(node3)
    node2.set_left(node4)
    node3.set_right(node5)


    s = Solution()
    preorder = s.preorderTraversal(node1)
    inorder = s.inorderTraversal(node1)
    postorder = s.postorderTraversal(node1)
    levelorder = s.levelorderTraversal(node1)
    
    print(f'preorder: {preorder}')
    print(f'inorder: {inorder}')
    print(f'postorder: {postorder}')
    print(f'levelorder: {levelorder}')
    