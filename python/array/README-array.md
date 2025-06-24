針對 **LeetCode Blind 75** 中與 **Array 主題** 相關題目的 **介紹、結論、比喻與簡單說明**，幫助你掌握核心觀念：

---

## 🔢 LeetCode Blind 75：Array 題型介紹與總結

### 🎯 **什麼是 Array 題目？**

Array（陣列）是一種最基本、最常見的資料結構，就像是一排排整齊擺放的櫃子，每個櫃子都有自己的編號（index），我們可以隨時快速地「指定編號」去拿裡面的資料。

在 LeetCode 中，Array 題目通常考驗以下能力：

* 資料的遍歷與操作（遍歷一維/二維陣列）
* 使用額外資料結構（像是 hash map、set）
* 雙指標（two pointers）技巧
* 滑動視窗（sliding window）
* 排序、搜尋（含 binary search）
* 動態規劃（Dynamic Programming）

---

## 🧠 **比喻：Array 就像排隊櫃子或火車車廂**

想像一列火車（array），每個車廂（element）上都有一個編號，我們可以：

* 一節一節走過去查看（遍歷）
* 檢查哪幾節車廂裡有什麼物品（查詢）
* 改變其中某節車廂的內容（修改）
* 根據某種規則移動人員或物品（演算法）

---

## 📌 常見技巧與對應題型

| 技巧             | 說明             | 例題編號     | 題目                           |
| -------------- | -------------- | -------- | ---------------------------- |
| HashMap        | 利用快速查找提升效率     | 1        | Two Sum                      |
| Two Pointers   | 兩個指標從頭尾或同時移動   | 4, 5, 18 | Container, 3Sum, Insert Int  |
| Sliding Window | 固定或變動視窗長度處理子陣列 | 2, 22    | Longest Substring, MinWindow |
| 排序 + 掃描        | 先排序再處理邊界條件     | 17, 73   | Merge Intervals, Non-overlap |
| Prefix Sum     | 累加和快速查詢        | 54       | Product of Array Except Self |
| Binary Search  | 已排序陣列中快速查找     | 10, 39   | Rotated Array, Find Minimum  |
| Greedy         | 動態記錄最小值/最大差值等  | 30       | Best Time to Buy/Sell Stock  |

---

## 🧩 **Array 題目的常見類型**

### 1. **找數字是否存在/位置**

* `Two Sum`（用 HashMap 記錄配對）
* `3Sum`（先排序，雙指標找解）

### 2. **找最大值、最小值或某種極值**

* `Container With Most Water`（雙指標逼近）
* `Maximum Subarray`（動態規劃求連續和）

### 3. **區間合併、處理**

* `Merge Intervals`、`Insert Interval`、`Non-overlapping Intervals`

### 4. **旋轉陣列或矩陣操作**

* `Rotate Image`（原地轉置+翻轉）
* `Find Minimum in Rotated Sorted Array`（二分搜尋變形）

---

## ✅ **結論與學習重點**

### 🎓 學會 Array 題目要掌握：

* **基本遍歷技巧（for loop, while loop）**
* **進階雙指標與滑動視窗技巧**
* **搭配 HashMap / Set 加快搜尋**
* **排序後處理邏輯 + 二分搜尋應用**
* **動態規劃觀念（如最大連續子陣列）**

---

## 📖 建議學習順序（由淺入深）

1. Two Sum（hash map 基礎）
2. Best Time to Buy and Sell Stock（紀錄最小值）
3. Maximum Subarray（DP 入門）
4. 3Sum（排序 + 雙指標）
5. Container With Most Water（雙指標經典）
6. Merge Intervals（排序合併邏輯）
7. Product of Array Except Self（前綴/後綴乘積技巧）
8. Search in Rotated Sorted Array（二分搜尋變形）


