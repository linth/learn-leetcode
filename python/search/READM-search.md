## LeetCode Blind 75：Search 主題題目核心觀念

### 介紹

在 LeetCode Blind 75 題庫中，「search」主題涵蓋了各種經典的搜尋技巧，像是線性搜尋、二分搜尋（binary search）、以及搜尋在特殊結構（如旋轉排序陣列、二元樹、圖）中的應用。這些題目不僅考驗你對搜尋演算法的熟練度，更強調你能否根據資料結構特性選擇最有效率的搜尋方式[6][7][8]。

---

### 結論

熟練 Blind 75 的 search 題目，能幫助你：
- 快速判斷何時該用線性搜尋、何時該用二分搜尋。
- 掌握如何在排序陣列、旋轉陣列、樹、圖等不同資料結構中設計搜尋流程。
- 提升解題效率，寫出時間複雜度更低的程式。
- 建立面對未知問題時的「分治」、「縮小範圍」等思維模式[7][8]。

---

### 比喻

可以把搜尋比喻成「找東西」：
- **線性搜尋**像是翻箱倒櫃一個個找，效率較低。
- **二分搜尋**就像是在有序的書架上找書，每次都能排除一半的書，速度快很多。
- **在旋轉排序陣列中搜尋**，就像書架被人打亂了一部分，你要先判斷哪一段還是有序，再決定往哪邊找[7]。

---

### 簡單說明

- **常見題型**：
  - 在排序陣列中搜尋（如 Search in Rotated Sorted Array）
  - 找陣列中的最小值（Find Minimum in Rotated Sorted Array）
  - 樹或圖的搜尋（BFS/DFS）
- **核心技巧**：
  - 二分搜尋：每次比較中間值，根據結果縮小搜尋範圍，時間複雜度 $$O(\log n)$$。
  - 線性搜尋：逐一檢查每個元素，時間複雜度 $$O(n)$$。
  - 搜尋時要根據資料結構特性（如是否有序、是否有重複、是否有環）調整演算法。
- **經典例題**：
  - Search in Rotated Sorted Array：考驗你判斷哪一半有序，並正確移動指標[5][7]。
  - Find Minimum in Rotated Sorted Array：利用二分搜尋找最小值。
  - Binary Search Tree 的搜尋：利用樹的有序特性快速定位。

---

> **總結：**  
> Search 題目考驗你「如何有效率地找東西」的能力。就像在圖書館找書，如果你知道分類法（排序），就能用二分搜尋快速找到；如果一切都亂了，只能一個個找。熟悉各種搜尋技巧，是寫出高效程式、通過面試的關鍵[7][8]。

[1] https://neetcode.io/practice?tab=blind75
[2] https://takeuforward.org/interviews/blind-75-leetcode-problems-detailed-video-solutions
[3] https://www.techinterviewhandbook.org/best-practice-questions/
[4] https://leetcode.com/problem-list/oizxjoit/
[5] https://www.youtube.com/watch?v=KzKVa5sBPjc
[6] https://algorithms.theroyakash.com/blind75/
[7] https://www.youtube.com/watch?v=o7qCzQOmdBA
[8] https://github.com/jaimin-bariya/blind-75-leetcode
[9] https://www.youtube.com/watch?v=L51xE6y-KWY
[10] https://mohsentabibian.github.io/LeetCode-Solutions/15.%20Greedy/README.html
[11] https://github.com/amrita150/Blind-75-LeetCode-Questions
[12] https://www.dotnetinterviews.com/blind-75-leetcode-problems
[13] https://www.youtube.com/playlist?list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf
[14] https://www.greatfrontend.com/interviews/blind75
[15] https://github.com/SwarajShelavale/LeetCode-Blind-75
[16] https://github.com/gosiqueira/blind-75
[17] https://takeuforward.org/interviews/blind-75-leetcode-problems-detailed-video-solutions/



---
針對 **LeetCode Blind 75** 中與 **Search 主題（搜尋）** 相關的題目的：

* 📘 主題介紹
* ✅ 解題結論
* 🎯 日常比喻
* ✏️ 簡單說明

快速掌握「搜尋」在 LeetCode 題目中的核心技巧與應用邏輯。

---

## 🔍 Search 主題在 Blind 75 題中的涵蓋類型

Search 在 Blind 75 中主要分為三種型態：

| 搜尋類型                       | 特點與應用範圍           |
| -------------------------- | ----------------- |
| ✅ **Binary Search（二分搜尋）**  | 快速定位排序資料中的元素      |
| ✅ **DFS / BFS（深度/廣度優先搜尋）** | 用於圖、網格、樹、找路徑或區塊   |
| ✅ **Backtracking（回溯）**     | 用於組合、排列、迷宮問題等路徑搜索 |

---

## ✅ Search 題目總覽（Blind 75 中）

| 題號 | 題目名稱                           | 搜尋類型                   |
| -- | ------------------------------ | ---------------------- |
| 1  | Binary Search                  | Binary Search          |
| 2  | Search in Rotated Sorted Array | Binary Search          |
| 3  | Koko Eating Bananas            | Binary Search + 模擬     |
| 4  | Number of Islands              | BFS / DFS              |
| 5  | Word Search                    | DFS + 回溯               |
| 6  | Pacific Atlantic Water Flow    | BFS + DFS              |
| 7  | Clone Graph                    | BFS / DFS              |
| 8  | Course Schedule                | Topological Sort (BFS) |
| 9  | Subsets                        | Backtracking           |
| 10 | Combination Sum                | Backtracking           |
| 11 | Permutations                   | Backtracking           |

---

## 🧠 結論總整理：三種 Search 的使用時機

| 類型                | 使用時機           | 時間複雜度          | 重點技巧           |
| ----------------- | -------------- | -------------- | -------------- |
| **Binary Search** | 處理排序陣列，找值/區間   | O(log n)       | 不斷縮小左右邊界       |
| **DFS / BFS**     | 圖、網格、樹的走訪、區塊探索 | O(n)           | visited 標記避免重複 |
| **Backtracking**  | 所有組合/排列/解空間探索  | O(2ⁿ) or worse | 決策樹 + 剪枝策略     |

---

## 🎨 比喻幫助理解

| 搜尋類型          | 比喻                        |
| ------------- | ------------------------- |
| Binary Search | 像在字典中找單字，翻開中間頁開始比對        |
| BFS           | 像是多層電梯，逐層探查鄰居             |
| DFS           | 像是走迷宮，一路往下走到底，再回頭         |
| Backtracking  | 像是在解 Sudoku：試一個 → 不對就回頭再試 |

---

## ✏️ 重點題目簡單說明（含技巧）

---

### 1️⃣ Binary Search

* **比喻**：像翻字典 → 先翻中間頁
* **技巧**：

  * 有序陣列才能使用
  * 計算 mid，決定往左或右縮小搜尋空間
* **常見陷阱**：避免 `left = mid` 無限迴圈，應設 `left = mid + 1`

---

### 2️⃣ Search in Rotated Sorted Array

* **比喻**：像是在斷裂的排序陣列中找數字
* **技巧**：二分時判斷哪一半是有序的，再根據目標判斷往哪邊走

---

### 3️⃣ Koko Eating Bananas

* **比喻**：像試不同速度吃香蕉 → 哪個速度剛好能在時限內吃完
* **技巧**：用 binary search 嘗試「速度」，模擬總時間是否滿足

---

### 4️⃣ Number of Islands

* **比喻**：你是一個探險家，每次踏上新陸地，就用 DFS/BFS 探索整座島
* **技巧**：從每個未拜訪的「1」開始搜尋，把整塊區域標記拜訪過

---

### 5️⃣ Word Search

* **比喻**：在字母迷宮裡，嘗試走出一個單字路徑
* **技巧**：

  * 每格嘗試起點，沿著上下左右 DFS
  * 使用回溯（訪問 → 試走 → 回退）

---

### 6️⃣ Clone Graph

* **比喻**：你是一個複製機器人，從一個節點出發複製整張圖
* **技巧**：

  * BFS or DFS 均可
  * 使用 visited map 避免無限循環 & 重複 clone

---

### 7️⃣ Course Schedule

* **比喻**：修課順序要合法，就像排課一樣 → 沒有循環才可以全部修完
* **技巧**：

  * 建立 in-degree array
  * 用 queue 做 Topological Sort 判斷是否有環

---

### 8️⃣ Subsets / Combination Sum / Permutations

* **比喻**：在排列組合世界中走迷宮，嘗試所有可能的決策組合
* **技巧**：

  * 遞迴＋回溯 + 剪枝
  * Subsets: 每個元素選或不選
  * Combination: sum 要等於 target
  * Permutations: 所有順序都試過一輪

---

## 🛠 Search 的通用模板概念（面試一定要會）

### 🔍 Binary Search 模板：

```ts
let left = 0, right = arr.length - 1;
while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] == target) return mid;
    else if (arr[mid] < target) left = mid + 1;
    else right = mid - 1;
}
return -1;
```

---

### 🧗 DFS 模板（遞迴）：

```ts
function dfs(node) {
  if (!node) return;
  visited.add(node);
  for (let neighbor of node.neighbors) {
    if (!visited.has(neighbor)) dfs(neighbor);
  }
}
```

---

### 🚶 BFS 模板（queue）：

```ts
const queue = [start];
const visited = new Set();
while (queue.length > 0) {
  const node = queue.shift();
  for (let neighbor of node.neighbors) {
    if (!visited.has(neighbor)) {
      visited.add(neighbor);
      queue.push(neighbor);
    }
  }
}
```

---

### 🔁 Backtracking 模板：

```ts
function backtrack(path, choices) {
  if (滿足結束條件) {
    result.push([...path]);
    return;
  }

  for (let i = 0; i < choices.length; i++) {
    path.push(choices[i]);
    backtrack(path, choices);
    path.pop(); // 回退
  }
}
```

---

## ✅ 學習建議總結

| 任務           | 說明                          |
| ------------ | --------------------------- |
| 📘 熟悉三種搜尋題型  | 二分搜尋、DFS/BFS、Backtracking   |
| 🧠 練會比喻與口語講解 | 面試時幫你釐清邏輯並留下好印象             |
| 🧪 多練題型轉換    | 同一題可以用 DFS / BFS / 回溯多種寫法練習 |
| 🧩 學會模組化模板   | 每種搜尋都有「固定套路」可以簡化記憶          |



