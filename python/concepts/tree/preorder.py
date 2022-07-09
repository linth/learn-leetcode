
"""
Preorder traversal 


Reference:
    - https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0144.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%89%8D%E5%BA%8F%E9%81%8D%E5%8E%86.md
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 栈迭代遍历
    
    def preorderTraversal(self, root):
        if not root:
            return []
        
        res = []
        stack = [root]
                
        while stack:
            node = stack.pop() # 因為只有一個資料
            res.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


if __name__ == '__main__':
    # root = [1, null, 2, 3]

    # s = Solution()
    # res = s.preorderTraversal(root)
    # print('res: ', res)
    pass