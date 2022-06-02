'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Reference:
    - https://www.youtube.com/watch?v=pUSy6UZCFKw&t=1s
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]):
        # recursive
        # return self.use_recursive(root)
    
        # iterative
        return self.use_iterative(root)
        
    def use_recursive(self, root):
        if not root:
            return []
                
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
    def use_iterative(self, root):
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
    
    
if __name__ == '__main__':
    
    s = Solution()
    root = [1,null,2,3]
    res = s.preorderTraversal(root)
    print('res', res)
    