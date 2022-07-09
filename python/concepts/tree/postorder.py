# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root):
        
        res, stack = [], []
        prev = None
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
                
            node = stack.pop()
            
            if not node.right or node.right == prev:
                res.append(node.val)
                prev = node
                root = None
            else:
                stack.append(node)
                root = node.right
        return res

if __name__ == '__main__':
    
    node3 = TreeNode(3)
    node2 = TreeNode(2, TreeNode(4), TreeNode(5))
    node1 = TreeNode(1, node2, node3)
    
    s = Solution()
    res = s.postorderTraversal(node1)
    print('res', res)
    