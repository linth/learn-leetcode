# Binary Tree Traversal 二元樹遍歷
遍歷二元樹 (Binary Tree Traversal) 的 Traversal 順序有三種，分別是
- 前序 (preorder), [refer to youtube]()
- 中序 (inorder), [refer to youtube](https://www.youtube.com/watch?v=dM7Rib6hjsc)
- 後序 (postorder), [refer to youtube]()
- Level-Order

遍歷二元樹實作又可以分為遞迴 (recursive) 和迭代 (iterative) 兩種版本，本篇文章將介紹迭代遍歷二元樹 (iterative binary tree traversal) 的三種方法。

```
    4
   / \
  2   6
 / \ / \
1  3 5  7
```

前序 (preorder): 中 -> 左 -> 右，4213657
中序 (inorder): 左 -> 中 -> 右，1234567。注意：對二元搜尋樹 (binary search tree, BST) 做 inorder traversal 就是由小到大依序遍歷。
後序 (postorder): 左 -> 右 -> 中，1325764
Level-Order: 4261357，是照著「level由小到大」的順序，由上而下，並在同一個level「由左至右」依序Visiting每個node。

前序、中序、後序的順序差異在於 中間放在那邊?
    - 前: 中間放第一個
    - 中: 中間放第二個
    - 後: 中間放第三個

[!](https://assets.leetcode.com/users/andvary/image_1556551007.png)

## Reference
- https://shubo.io/iterative-binary-tree-traversal/
- https://github.com/itcharge/LeetCode-Py/blob/main/Solutions/0144.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%89%8D%E5%BA%8F%E9%81%8D%E5%8E%86.md
- http://alrightchiu.github.io/SecondRound/binary-tree-traversalxun-fang.html#bttraversal