'''

Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root): 
        # recursive method.
        # return self.use_recursive(root)
    
        # iterative method.
        return self.use_iterative(root)
    
    def use_recursive(self, root):
        if root is None:
            return []
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    
    
    def use_iterative(self, root):
        # left, right, root
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            
            if node:
                result.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return result[::-1]
    
    # def use_iterative(self, root):
        
    #     res, stack = [], []
    #     prev = None
        
    #     while root or stack:
    #         while root:
    #             stack.append(root)
    #             root = root.left
                
    #         node = stack.pop()
            
    #         if not node.right or node.right == prev:
    #             res.append(node.val)
    #             prev = node
    #             root = None
    #         else:
    #             stack.append(node)
    #             root = node.right
    #     return res


if __name__ == '__main__':
    
    root = [1,null,2,3]
    s = Solution()
    res = s.postorderTraversal(root)
    print('res', res)

