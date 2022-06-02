'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        
        if root is None:
            return []
        
        # queue = [node, node.left, node.right]
        # next_queue = [node.left, node.right]
        # level = [node.val]
        
        # result = level
        # leve = []
        # queue = next_queue
        # next_queue = []
        
        queue, next_queue = [root], []
        level, result = [], []
        
        while queue != []:
            for root in queue:
                level.append(root.val)
                
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
                    
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []
        return result


if __name__ == '__main__':
    # recommendation to watch the youtube video at first.
    # https://www.youtube.com/watch?v=MBZ-gBkjdMc
    
    # another ways to solve it, please refer to the URL as follows:
    # https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33464/5-6-lines-fast-python-solution-(48-ms)
    
    s = Solution()
    root = [3,9,20,null,null,15,7]
    res = s.levelOrder(root)
    print('res', res)