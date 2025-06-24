## LeetCode Blind 75：Sorting 主題題目核心觀念

### 介紹

在 LeetCode Blind 75 題庫中，**sorting（排序）** 是一個基礎且重要的主題，涵蓋多種排序技巧與應用場景。排序不僅是資料整理的基本操作，也是許多演算法（如雙指標、二分搜尋、滑動視窗）能高效運作的前提。Blind 75 中的排序題目多數結合了雙指標技巧、排序後的搜尋與組合問題，幫助你掌握排序的核心概念與實務應用。

---

### 結論

透過練習 Blind 75 中的排序題目，你能：
- 熟悉各種排序演算法的特性與時間複雜度（如快速排序、合併排序、內建排序）。
- 掌握排序後如何用雙指標技巧解決問題（如兩數之和、三數之和）。
- 理解排序在優化搜尋與組合問題中的關鍵作用。
- 增強解題時結合排序與其他技巧（雙指標、二分搜尋）的能力。

---

### 比喻

排序就像是把一堆亂放的書本依照字母順序或大小分類擺放整齊：
- **排序**是把書架整理好，方便你快速找到想要的書。
- **雙指標技巧**就像用兩根手指同時從書架兩端往中間找目標書，效率比一根手指慢慢找快得多。
- 排序後的搜尋就像你知道書本已經排好序，能用快速查找法（例如二分搜尋）迅速定位。

---

### 簡單說明

- **常見題型**：
  - 兩數之和（Two Sum）在排序陣列上的雙指標解法。
  - 三數之和（3Sum）利用排序與雙指標找三個數字組合。
  - 合併多個排序陣列（Merge K Sorted Lists）。
- **核心技巧**：
  - 先排序再用雙指標縮小搜尋範圍，提升效率。
  - 利用排序結果快速跳過重複元素，避免重複計算。
  - 理解排序演算法的時間複雜度與空間使用，選擇合適方法。
- **時間複雜度**：
  - 排序通常是 $$O(n \log n)$$。
  - 雙指標搜尋通常是 $$O(n)$$。
  - 結合後的解法多為 $$O(n^2)$$（如 3Sum）。

---

> **總結：**  
> Sorting 是解決許多複雜問題的基石。就像把書本整理好才能快速找到目標，排序讓你能用雙指標、二分搜尋等高效技巧，快速解決組合與搜尋問題。熟練排序與雙指標的搭配，是面試中不可或缺的核心能力。

---

（以上內容結合了 Blind 75 題庫的排序相關題目特性與常見解題策略，幫助你快速掌握排序主題的核心觀念。）

[1] https://neetcode.io/practice?tab=blind75
[2] https://leetcode.com/discuss/general-discussion/460599/leetcode-solution-index/
[3] https://github.com/SwarajShelavale/LeetCode-Blind-75
[4] https://takeuforward.org/interviews/blind-75-leetcode-problems-detailed-video-solutions
[5] https://www.youtube.com/watch?v=KzKVa5sBPjc
[6] https://www.youtube.com/watch?v=L51xE6y-KWY
[7] https://dmytros.blog/posts/leetcode-blind-75-reorder-list/
[8] https://github.com/jaimin-bariya/blind-75-leetcode


---

針對 **LeetCode Blind 75 中的 Sorting 主題題目**，提供的：

* 📘 **主題介紹**
* ✅ **結論歸納**
* 🎯 **日常比喻**
* ✏️ **簡單說明與策略整理**

掌握排序（Sorting）在常考題中的應用方式與背後邏輯。

---

## 🔢 Sorting 在 Blind 75 中的常見題型

雖然「純排序實作」不常考（例如 Merge Sort, Quick Sort），但排序是許多題目的**前置動作**或**關鍵策略**。

| 題號  | 題目名稱                            | 排序在其中的作用                |
| --- | ------------------------------- | ----------------------- |
| 1️⃣ | Merge Intervals                 | 排序 + 合併邏輯（按 start）      |
| 2️⃣ | Insert Interval                 | 排序 + 區間合併               |
| 3️⃣ | Meeting Rooms II                | 排序 + 優先隊列處理時間衝突         |
| 4️⃣ | Top K Frequent Elements         | 排序 + Heap               |
| 5️⃣ | Kth Largest Element in an Array | 排序 + QuickSelect / Heap |
| 6️⃣ | Merge K Sorted Lists            | 多個排序資料串，需合併處理           |
| 7️⃣ | Sort Colors                     | 排序邏輯（荷蘭國旗問題）            |
| 8️⃣ | Largest Number                  | 自定排序規則（字串比較）            |

---

## ✅ 結論歸納：Sorting 是「轉換問題型態」的技巧

| 場景                     | 為什麼排序有用               |
| ---------------------- | --------------------- |
| 區間合併（Intervals）        | 讓資料有序後更容易合併重疊、處理邊界    |
| 頻率統計（Top K）            | 排序後能快速取得高頻元素或最大值      |
| 多序列合併（Merge Lists）     | 排序後便於使用 Heap 處理多個有序串流 |
| 特殊順序需求（Largest Number） | 自定排序規則能轉換比較邏輯         |

---

## 🎨 排序的日常比喻

| 題型類別                 | 生活比喻                        |
| -------------------- | --------------------------- |
| Merge Intervals      | 整理行事曆上的會議時間，避免時間重疊          |
| Top K 頻率元素           | 統計最常聽的 Spotify 歌曲，按播放次數排前幾名 |
| Kth Largest Element  | 比賽中選出第 K 名選手，不用全排，只要找到第 K 大 |
| Merge K Sorted Lists | 像從多條已排序的馬拉松選手清單合併成一個完整排名    |
| Sort Colors          | 荷蘭國旗問題：把顏色分類整齊，按順序排列（紅、白、藍） |

---

## ✏️ 題目解析與簡單說明

---

### 1️⃣ Merge Intervals

* **核心技巧**：先按 `start` 進行排序，再逐一合併重疊區間
* **範例**：

  ```ts
  intervals.sort((a, b) => a[0] - b[0]);
  ```
* **關鍵思維**：排序是為了讓區間「有序可控」，合併就簡單許多

---

### 2️⃣ Insert Interval

* **延伸自 Merge Intervals**，只是先插入一筆資料再做排序與合併
* **流程**：

  1. 插入新區間
  2. 整體排序
  3. 跑一輪合併邏輯

---

### 3️⃣ Meeting Rooms II

* **問題**：最少需要幾間會議室才不會有時間衝突
* **技巧**：

  * 把開始與結束時間分別排序
  * 雙指針追蹤會議開始與結束的交替狀況

---

### 4️⃣ Top K Frequent Elements

* **解法**：

  1. 用 HashMap 統計頻率
  2. 將頻率丟入 Heap（或 Bucket）排序
* **目標**：找出前 K 高頻元素

---

### 5️⃣ Kth Largest Element

* **策略**：

  * 使用 Min Heap（保持 K 個最大元素） → O(n log k)
  * 或 QuickSelect 分治法 → O(n) 平均時間
* **不是直接排序再取值，效率太低（O(n log n)）**

---

### 6️⃣ Merge K Sorted Lists

* **關鍵技巧**：

  * 使用 Min Heap 同時追蹤每條 list 的當前最小節點
  * 持續取出最小值並更新來源 list 的下個節點

---

### 7️⃣ Sort Colors（荷蘭國旗問題）

* **目標**：對 0、1、2 做 in-place 排序
* **技巧**：使用三指針（left, right, i）一次掃描處理所有顏色
* **屬於「不用真的排序」但考驗邏輯的題型**

---

### 8️⃣ Largest Number

* **目標**：將數字陣列排序成能組成最大整數的順序（字串拼接最大）
* **技巧**：自定排序規則 → 比較 `a + b` vs `b + a` 誰大

---

## 🛠 排序策略總結對照表

| 題型           | 技巧核心      | 排序方式 / 策略                  |
| ------------ | --------- | -------------------------- |
| 區間處理         | 合併 + 排序   | 依 `start` 進行排序             |
| Top K / 頻率統計 | 排序 + Heap | HashMap + Heap or Bucket   |
| 特定位置（第 K 大）  | 快速選取      | QuickSelect or Heap        |
| Merge 多排序列表  | 合併排序      | Min Heap 處理多序列             |
| 特殊邏輯排序       | 自定排序規則    | 排序字串拼接邏輯（如 Largest Number） |
| 原地分類排序       | 指針分類法     | 三指針 → 荷蘭國旗問題               |

---

## ✅ 學習建議與策略

| 建議                                           | 說明                                 |
| -------------------------------------------- | ---------------------------------- |
| 練習使用 `Array.prototype.sort()` 的自定 comparator | JS/TS 語言使用時要靈活                     |
| 熟悉「排序 → 分組/合併」的思維套路                          | 類似區間題會很常用                          |
| 排序 + Heap/Bucket 是 Top K 題型關鍵                | 練習 HashMap 搭配使用                    |
| 學會「不是真的排序」的技巧（如 Sort Colors）                 | 模擬排序 but in-place 邏輯題              |
| 熟悉排序與資料結構的結合題型                               | 如 Merge K Lists + Heap、Top K + Map |




