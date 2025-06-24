## LeetCode Blind 75：Recursion 主題題目核心觀念

### 介紹

遞迴（Recursion）是解決許多經典演算法問題的核心技巧，尤其在樹、組合、分治、回溯等題型中廣泛應用。Blind 75 中的遞迴題目涵蓋從簡單的樹結構遍歷、反轉，到複雜的組合總和（Combination Sum）、動態規劃優化等，幫助你建立用「分解問題」的思維模式。

---

### 結論

掌握遞迴主題能讓你：

- 理解如何將大問題拆解成小問題，並用相同邏輯反覆解決。  
- 熟悉遞迴函式的結構：基底條件（base case）與遞迴呼叫（recursive call）。  
- 練習回溯（backtracking）技巧，解決組合、排列等需探索所有可能性的問題。  
- 學會使用記憶化（memoization）或動態規劃優化遞迴，提升效率。

---

### 比喻

遞迴就像「鏡中鏡」的無限反射：  
- 你要解決一個問題，先把它拆成更小的同類問題，然後再拆更小，直到問題變得非常簡單（基底條件），再逐層回傳結果。  
- 就像爬樓梯時，先爬一階，再爬下一階，直到到達頂樓，每一步都依賴前一步的結果。

---

### 簡單說明

- **基底條件**：遞迴必須有停止條件，避免無限呼叫。  
- **遞迴呼叫**：函式內呼叫自己，解決子問題。  
- **回溯**：在嘗試不同選項時，遞迴結束後回到上一層，嘗試其他可能。  
- **典型題目**：  
  - 二元樹遍歷與反轉（Invert Binary Tree）  
  - 組合總和（Combination Sum）  
  - 最長遞增子序列（Longest Increasing Subsequence）  
  - 子集、排列問題  
- **優化技巧**：利用記憶化避免重複計算，將時間複雜度從指數級降低到多項式級。

---

> **總結：**  
> 遞迴是解決複雜問題的強大工具，核心在於「分而治之」的思維。透過基底條件控制遞迴深度，並善用回溯探索所有可能，搭配記憶化優化，能有效解決面試中常見的組合與樹形結構問題。

---

此說明結合 Blind 75 遞迴題目特性與常見解題策略，幫助你快速掌握遞迴的核心觀念與實務應用。

[1] https://takeuforward.org/interviews/ blind-75-leetcode-problems-detailed-video-solutions \
[2] https://www.youtube.com/watch?v=L51xE6y-KWY \
[3] https://hackmd.io/@meyr543/HJvvgvjyq \
[4] https://dmytros.blog/posts/leetcode-blind-75-longest-increasing-subsequence/ \
[5] https://www.youtube.com/watch?v=t5W-TwBr-zc \
[6] https://dmytros.blog/posts/leetcode-blind-75-combination-sum/ \
[7] https://www.youtube.com/watch?v=PieZjz2Pyhw \
[8] https://neetcode.io/practice?tab=blind75

---


針對 **LeetCode Blind 75 中與 Recursion 主題** 相關題目的系統性說明，包括：

* 📘 主題介紹
* ✅ 結論歸納
* 🎯 日常比喻
* ✏️ 每題簡單說明與策略

---

## 📘 一、主題介紹：Recursion 是什麼？

**Recursion（遞迴）** 是讓一個函數「呼叫自己」的技巧。
它通常用來處理問題可以被**分割成相同型態的子問題**時。

典型結構：

```ts
function recurse(params) {
  if (baseCase) return result;   // 終止條件
  result = recurse(smallerInput) // 遞迴呼叫
  return result;
}
```

---

## ✅ 二、結論：掌握「終止條件 + 子問題組裝」是遞迴的關鍵

| 構成要素           | 說明                    |
| -------------- | --------------------- |
| Base Case      | 避免無限遞迴（例如空陣列、null 節點） |
| Recursive Step | 問題拆分為更小的同型子問題         |
| 回傳值組合          | 將子問題結果合併為整體解（例如左 + 右） |

---

## 🎯 三、Recursion 的日常比喻

| 題型                    | 比喻                     |
| --------------------- | ---------------------- |
| Binary Tree Traversal | 從樹的根開始問左邊孩子，再問右邊孩子     |
| Permutations / 組合     | 做決策樹：每一層選一個元素的排列       |
| Fibonacci / DP 初型     | 走樓梯：每次只能走一步或兩步，看總共幾種走法 |
| 路徑總和                  | 每個節點都問：你這邊有到目標的路徑嗎？    |

---

## 📚 四、Blind 75 中遞迴題目列表

| 題目名稱                          | 主題類型              | 核心技巧          |
| ----------------------------- | ----------------- | ------------- |
| Invert Binary Tree            | Binary Tree 遞迴    | 子節點交換         |
| Maximum Depth of Binary Tree  | Tree 深度計算         | 從葉子往上回傳       |
| Same Tree                     | 結構比對              | 左右子樹比對        |
| Subtree of Another Tree       | 結構遞迴比對            | 遞迴掃所有子節點      |
| Path Sum                      | 路徑累加計算            | 遞迴 + 減法       |
| Merge Two Sorted Lists        | List 合併           | 遞迴版 Merge     |
| Lowest Common Ancestor of BST | 分岔判斷遞迴            | 根據 BST 規則遞迴下去 |
| Balanced Binary Tree          | 遞迴計算 + early stop | 回傳高度 or false |
| Validate BST                  | 需帶上下界遞迴           | 中序 or 下界限制    |

---

## ✏️ 五、每題簡單說明與遞迴策略

---

### 🔹 Invert Binary Tree

* **目標**：左右子樹對調
* **遞迴策略**：先遞迴左、右 → 然後交換

```ts
function invert(node) {
  if (!node) return null;
  const left = invert(node.left);
  const right = invert(node.right);
  node.left = right;
  node.right = left;
  return node;
}
```

---

### 🔹 Maximum Depth of Binary Tree

* **目標**：計算樹的最大深度
* **遞迴策略**：每層加 1，傳回左右最大值

```ts
function maxDepth(node) {
  if (!node) return 0;
  return 1 + Math.max(maxDepth(node.left), maxDepth(node.right));
}
```

---

### 🔹 Same Tree

* **目標**：判斷兩棵樹是否完全相同
* **遞迴策略**：左右子樹逐層比對值與結構

```ts
function isSame(p, q) {
  if (!p && !q) return true;
  if (!p || !q || p.val !== q.val) return false;
  return isSame(p.left, q.left) && isSame(p.right, q.right);
}
```

---

### 🔹 Path Sum

* **目標**：有沒有一條從 root 到 leaf 的路徑，加總等於 target
* **遞迴策略**：每次減掉目前值 → 繼續往子節點找

---

### 🔹 Merge Two Sorted Lists

* **遞迴版思路**：

```ts
if (!l1) return l2;
if (!l2) return l1;
if (l1.val < l2.val) {
  l1.next = merge(l1.next, l2);
  return l1;
} else {
  l2.next = merge(l1, l2.next);
  return l2;
}
```

---

### 🔹 Subtree of Another Tree

* **思路**：對每個節點檢查是不是一樣的子樹（Same Tree 遞迴 + 掃描）

---

### 🔹 Lowest Common Ancestor of BST

* **思路**：利用 BST 屬性：

  * p, q 在兩邊 → return root
  * p, q 在同一邊 → 向該側遞迴

---

## 🧩 六、遞迴常見陷阱與處理技巧

| 問題類型                   | 解法說明                 |
| ---------------------- | -------------------- |
| 無終止條件導致 Stack Overflow | 加上 base case！        |
| 回傳值混亂                  | 明確定義「每一層要 return 什麼」 |
| 資料重複訪問效率差              | 加上 memoization（記憶化）  |
| 全排列類型要避開重複             | 使用 visited\[] 或排序剪枝  |

---

## ✅ 七、學習與練習建議

| 建議                           | 說明                             |
| ---------------------------- | ------------------------------ |
| 練習手寫基本模板                     | 包括 DFS、回傳計數、early stop、merge 等 |
| 練習 debug 遞迴流程（可畫 call stack） | 理解每層「誰叫誰、誰回來」的順序               |
| 嘗試轉換成迭代寫法（如樹遍歷）              | 加強對邏輯的掌控                       |
| 寫題前先明確定義 base case 與傳回值      | 保證每層遞迴的完整性與正確性                 |


