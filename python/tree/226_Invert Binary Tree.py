"""
Given the root of a binary tree, invert the tree, and return its root.

 
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
 

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Reference
    - https://leetcode.com/problems/invert-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode):
        
        # recursive method
        return self.use_recursive(root)
    
        # bfs method
        #return self.use_bfs(root)
        
        # dfs method
        #return self.use_dfs(root)
        
    
    def use_recursive(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
    
    def use_bfs(self, root):
        # bfs method
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
    
    def use_dfs(self, root):
        # dfs method
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])       
        return root


if __name__ == '__main__':
    root = [4,2,7,1,3,6,9]

    s = Solution()
    res = s.invertTree(root)
    print('res', res)






    
    