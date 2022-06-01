"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1
 

Constraints:
- The number of nodes in the tree is in the range [0, 104].
- -100 <= Node.val <= 100

Reference
    - https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode):
        # recursive method.
        if not root:
            return 0
                
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def use_iterative(self, root):
        # iterative method.
        if not root:
            return 0
        
        level = 0 # how many level.
        worklist = [root]
        num_node_level = 1 
        
        while worklist:
            node = worklist.pop(0)
            
            if node.left:
                worklist.append(node.left)                
            if node.right:
                worklist.append(node.right)
            
            num_node_level -= 1
            if num_node_level == 0:
                level += 1
                num_node_level = len(worklist)
        return level
    
if __name__ == '__main__':
    root = [0]

    s = Solution()
    res = s.maxDepth(root)
    print('res', res)

    
