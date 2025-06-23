# Question	Difficulty	Note

| #  | Question                                                     | Difficulty | Note                                                                 | Topic                |
|----|--------------------------------------------------------------|------------|----------------------------------------------------------------------|----------------------|
| 1  | Two Sum                                                      | Easy       | hash map                                                             | Array                |
| 2  | Longest Substring Without Repeating Characters              | Medium     | Sliding Window + HashMap                                             | String               |
| 3  | Longest Palindromic Substring                               | Medium     | DP : dp[i][j] 從i到j是否為palindromic string                         | String               |
| 4  | Container With Most Water                                   | Medium     | two-pointers                                                         | Array                |
| 5  | 3Sum                                                         | Medium     | three-pointers                                                       | Array                |
| 6  | Remove Nth Node From End of List                            | Medium     | fast slow pointers                                                   | LinkedList           |
| 7  | Valid Parentheses                                            | Easy       | stack                                                                | String               |
| 8  | Merge Two Sorted Lists                                      | Easy       | 使用dummy node和two pointers                                        | LinkedList           |
| 9  | Merge k Sorted Lists                                        | Hard       | 兩兩list合併，O(NlogK)                                               | LinkedList           |
| 10 | Search in Rotated Sorted Array                              | Medium     | rotated array，判斷左或右半邊有序                                     | Binary Search        |
| 11 | Combination Sum IV                                          | Medium     | DP: dp[i] 加到i的數目 = sum(i - sum[j])                             | Dynamic Programming  |
| 12 | Rotate Image                                                | Medium     | 有space O(1)的做法                                                  | Array                |
| 13 | Group Anagrams                                              | Medium     | 排序後字串當key                                                     | String               |
| 14 | Maximum Subarray                                            | Medium     | DP, dp[i] = max(dp[i - 1] + nums[i], nums[i])                        | Dynamic Programming  |
| 15 | Spiral Matrix                                               | Medium     | 右->下->左->上                                                       | Array                |
| 16 | Jump Game                                                   | Medium     | maxidx = max(maxidx, i + nums[i])                                   | Dynamic Programming  |
| 17 | Merge Intervals                                             | Medium     | 排序然後合併                                                        | Array                |
| 18 | Insert Interval                                             | Medium     | 判斷overlap並合併                                                   | Array                |
| 19 | Unique Paths                                                | Medium     | DP                                                                  | Dynamic Programming  |
| 20 | Climbing Stairs                                             | Easy       | DP                                                                  | Dynamic Programming  |
| 21 | Set Matrix Zeroes                                           | Medium     | 利用第一行第一列標記                                                | Array                |
| 22 | Minimum Window Substring                                    | Hard       | Sliding window                                                      | String               |
| 23 | Word Search                                                 | Medium     | Backtracking                                                        | Backtracking         |
| 24 | Decode Ways                                                 | Medium     | DP                                                                  | Dynamic Programming  |
| 25 | Validate Binary Search Tree                                 | Medium     | DFS, 使用(min, max)判斷BST                                          | Tree                 |
| 26 | Same Tree                                                   | Easy       | DFS                                                                 | Tree                 |
| 27 | Binary Tree Level Order Traversal                           | Medium     | 使用queue                                                           | Tree                 |
| 28 | Maximum Depth of Binary Tree                                | Easy       | Post-order traversal                                                | Tree                 |
| 29 | Construct Binary Tree from Preorder and Inorder Traversal   | Medium     | preorder找root, inorder分左右子樹                                   | Tree                 |
| 30 | Best Time to Buy and Sell Stock                             | Easy       | Greedy，每次記錄最小值                                              | Array                |
| 31 | Binary Tree Maximum Path Sum                                | Hard       | post-order                                                          | Tree                 |
| 32 | Valid Palindrome                                            | Easy       | two pointer, isalnum, tolower                                       | String               |
| 33 | Longest Consecutive Sequence                                | Medium     | HashSet接起來                                                       | Array                |
| 34 | Clone Graph                                                 | Medium     | 使用map記住新舊對應                                                 | Graph                |
| 35 | Word Break                                                  | Medium     | DP                                                                  | Dynamic Programming  |
| 36 | Linked List Cycle                                           | Easy       | fast-slow pointer                                                   | LinkedList           |
| 37 | Reorder List                                                | Medium     | 用Stack記錄ListNode                                                | LinkedList           |
| 38 | Maximum Product Subarray                                    | Medium     | DP最大值可能來自最小值乘負數                                       | Dynamic Programming  |
| 39 | Find Minimum in Rotated Sorted Array                        | Medium     | Binary Search                                                       | Binary Search        |
| 40 | Reverse Bits                                                | Easy       | 有O(1)解                                                            | Math                 |
| 41 | Number of 1 Bits                                            | Easy       | n = n & (n - 1)                                                     | Math                 |
| 42 | House Robber                                                | Medium     | DP: dp[i] = max(偷, 不偷)                                           | Dynamic Programming  |
| 43 | Number of Islands                                           | Medium     | DFS                                                                 | Graph                |
| 44 | Reverse Linked List                                         | Easy       | recursive                                                           | LinkedList           |
| 45 | Course Schedule                                             | Medium     | topological sort                                                    | Graph                |
| 46 | Implement Trie (Prefix Tree)                                | Medium     | unordered_map<char, node*>                                          | Trie                 |
| 47 | Design Add and Search Words Data Structure                  | Medium     | Trie + '.'通配符                                                    | Trie                 |
| 48 | Word Search II                                              | Hard       | Trie + Recursive                                                    | Backtracking         |
| 49 | House Robber II                                             | Medium     | DP: 額外變數處理首尾問題                                            | Dynamic Programming  |
| 50 | Contains Duplicate                                          | Easy       | 使用set                                                             | Array                |
| 51 | Invert Binary Tree                                          | Easy       | Preorder recursive                                                  | Tree                 |
| 52 | Kth Smallest Element in a BST                               | Medium     | inorder traversal                                                   | Tree                 |
| 53 | Lowest Common Ancestor of a BST                             | Easy       | 根據p、q和root的值判斷方向                                         | Tree                 |
| 54 | Product of Array Except Self                                | Medium     | Forward和backward vector                                           | Array                |
| 55 | Valid Anagram                                               | Easy       | 使用vector統計                                                     | String               |
| 56 | Meeting Rooms                                               | Easy       | 檢查是否有重疊                                                      | Interval             |
| 57 | Meeting Rooms II                                            | Medium     | priority_queue記錄最早結束的會議室                                 | Interval             |
| 58 | Graph Valid Tree                                            | Medium     | Union Find                                                          | Graph                |
| 59 | Missing Number                                              | Easy       | 用總和扣除                                                          | Math                 |
| 60 | Alien Dictionary                                            | Hard       | 拓撲排序                                                            | Graph                |
| 61 | Encode and Decode Strings                                   | Medium     | 轉成長度 + 分隔                                                    | String               |
| 62 | Find Median from Data Stream                                | Hard       | maxheap + minheap                                                   | Heap                 |
| 63 | Serialize and Deserialize Binary Tree                       | Hard       | Preorder + 文字串處理                                               | Tree                 |
| 64 | Longest Increasing Subsequence                              | Medium     | DP                                                                  | Dynamic Programming  |
| 65 | Coin Change                                                 | Medium     | dp[i] = min(dp[i], dp[i - c])                                       | Dynamic Programming  |
| 66 | Number of Connected Components in an Undirected Graph       | Medium     | Union Find                                                          | Graph                |
| 67 | Counting Bits                                               | Easy       | 用以前結果                                                         | Dynamic Programming  |
| 68 | Top K Frequent Elements                                     | Medium     | Map或Bucket Sort                                                   | Heap                 |
| 69 | Sum of Two Integers                                         | Medium     | 位元運算: a ^ b, (a & b) << 1                                      | Math                 |
| 70 | Pacific Atlantic Water Flow                                 | Medium     | BFS兩邊灌水                                                         | Graph                |
| 71 | Longest Repeating Character Replacement                     | Medium     | Sliding window                                                      | String               |
| 72 | Non-overlapping Intervals                                   | Medium     | 排序後刪掉end最大的                                                | Interval             |
| 73 | Subtree of Another Tree                                     | Easy       | serialize後比對                                                     | Tree                 |
| 74 | Palindromic Substrings                                      | Medium     | DP: dp[i][j]表示是否為回文子字串                                   | String               |
| 75 | Word Search                                                 | Medium     | Backtracking                                                        | Backtracking         |
