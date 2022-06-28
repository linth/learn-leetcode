
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        
        res, stack = [], []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res



if __name__ == '__main__':
    
    node3 = TreeNode(3)
    node2 = TreeNode(2, TreeNode(4), TreeNode(5))
    node1 = TreeNode(1, node2, node3)
    
    s = Solution()
    res = s.inorderTraversal(node1)
    print('res', res)
    # write some unit test code.
    