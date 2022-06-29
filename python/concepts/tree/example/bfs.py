'''
BFS 廣度優先搜尋演算法
    - 首先他是個演算法，換言之，可以使用他的概念在不同的資料結構下查詢排列。
    - 通常運用此演算法的有 graph 和 tree
    

Reference:
    - https://medium.com/%E7%A8%8B%E5%BC%8F%E4%B9%BE%E8%B2%A8/binarytree-%E5%BB%A3%E5%BA%A6%E6%90%9C%E5%B0%8Bbfs-vs-%E6%B7%B1%E5%BA%A6%E6%90%9C%E5%B0%8Bdfs-ad51a9ca5d68
'''
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
   

def bfs_tra(root):
    #! 此答案是錯誤，需思考 why。
    res = []
    queue = [root]
    
    while queue:
        node = queue.pop()
        res.append(node.val)
        
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    return res


def bfs_tra2(root):
    result = []
    q = queue.Queue()
    q.put(root)
    
    while q.qsize()>0:
        node = q.get()
        result.append(node.val)
        if node.left != None:
            q.put(node.left)
        if node.right != None:
            q.put(node.right)   
    return result
   
        
c1l = TreeNode(3)
c1r = TreeNode(4)
c2l = TreeNode(4)
c2r = TreeNode(3)
c1 = TreeNode(2, c1l, c1r)
c2 = TreeNode(2, c2l, c2r)
r = TreeNode(1, c1, c2)


print(bfs_tra(r))
print(bfs_tra2(r))


# 請注意寫法，當 argument 某項不給數值，會按照 default 給。
root = TreeNode(2, right=c2)
print(root.left) # None

