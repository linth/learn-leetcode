"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 
Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [1,2]
 

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
 

Follow up:
Recursive solution is trivial, could you do it iteratively?

Reference
    - https://leetcode.com/problems/binary-tree-inorder-traversal/
    - (youtube) https://www.youtube.com/watch?v=RJhh3Jcc9zw
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # for recursive
        # return self.use_recursive(root)
    
        # for iterative
        return self.use_iterative(root)
        
    def use_recursive(self, root):
        if not root:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
    
    
    def use_iterative(self, root):
        
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

if __name__ == '__main__':
    s = Solution()
    root = [1,null,2]
    res = s.inorderTraversal(root)
    print('res', res)
