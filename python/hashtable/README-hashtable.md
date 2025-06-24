## LeetCode Blind 75：Hash Table 主題題目核心觀念

### 介紹

Hash Table（雜湊表）是解決許多經典問題的基礎資料結構，Blind 75 中的 Hash Table 題目涵蓋數組元素搜尋、重複元素判斷、異位詞分組、兩數之和等。Hash Table 以其平均常數時間複雜度的查找特性，幫助你高效解決需要快速查詢和頻率統計的問題。

---

### 結論

熟練 Hash Table 題目可以讓你：

- 理解 Hash Table 的基本原理與操作（插入、查找、刪除）。  
- 利用 Hash Table 快速定位元素，降低時間複雜度至 O(n) 或更優。  
- 熟悉如何用 Hash Table 解決頻率統計、重複判斷、配對問題。  
- 掌握設計鍵值對結構來解決字串與數組相關問題。  
- 增強面試中對資料結構選擇與優化的判斷力。

---

### 比喻

Hash Table 就像一本「快速索引的字典」：

- 你想找一本書（元素），不用一頁頁翻，而是直接透過書名（key）快速定位到書架上的位置（value）。  
- 當你需要統計某個字母出現幾次，就像在字典中查找該字母條目，快速得知數量。  
- 解決兩數之和問題時，Hash Table 就像一張「朋友清單」，你快速查看是否有朋友的數字能和你組成目標和。

---

### 簡單說明

- **基本操作**：  
  - **插入**：將元素及其相關資訊存入 Hash Table 中。  
  - **查找**：透過 key 快速找到對應的 value。  
  - **刪除**：移除特定 key 及其 value。  
- **常見應用**：  
  - Two Sum：用 Hash Table 存差值，快速找配對元素。  
  - Contains Duplicate：用 Hash Set 檢查重複元素。  
  - Valid Anagram：統計字母頻率，判斷兩字串是否為異位詞。  
  - Group Anagrams：將異位詞分組，key 可用排序後字串或字母頻率。  
- **時間複雜度**：平均為 O(n)，因為查找與插入是常數時間。  
- **空間複雜度**：O(n)，需額外空間存放元素與頻率。

---

> **總結：**  
> Hash Table 是面試中解決快速查找與頻率統計問題的利器。透過將元素映射到鍵值對，能大幅提升搜尋效率。將 Hash Table 比喻為快速索引的字典，有助於理解其查找原理與應用場景，是掌握 Blind 75 中多數 Array 與 String 題目的關鍵。

---

此說明結合多個 Blind 75 Hash Table 題目與解題策略，幫助你快速掌握核心觀念與實務技巧。

[1] https://ithelp.ithome.com.tw/m/articles/10287100 \
[2] https://www.youtube.com/watch?v=JlbhUhTec-s \
[3] https://leetcode.com/problem-list/hash-table/ \
[4] https://swiftrefresher.com/leetcode/blind-75-arrays \
[5] https://www.youtube.com/watch?v=KzKVa5sBPjc \
[6] https://www.youtube.com/watch?v=PieZjz2Pyhw \
[7] https://www.youtube.com/watch?v=kyEbYOK9R0E \
[8] https://dmytros.blog/posts/leetcode-blind-75-missing-number/ 

---

針對 **LeetCode Blind 75 中與 Hash Table 主題** 題目的完整整理，包括：

* 📘 主題介紹
* ✅ 解題結論
* 🎯 比喻類比
* ✏️ 常見題目與核心策略

---

## 📘 一、主題介紹：什麼是 Hash Table？

Hash Table（雜湊表）是一種透過**Key-Value** 快速查找資料的結構，常見實作：

* JavaScript → `Map`, `Object`
* Python → `dict`
* Java → `HashMap`

**主要特性**：

* 插入 / 查找 / 刪除平均時間複雜度：**O(1)**
* 非序列化（無順序）
* 可透過雜湊函數解決搜尋效率問題

---

## ✅ 二、解題結論：善用 Hash Table ＝ 降維打擊

Hash Table 在解題中的用途：

| 用途             | 說明                  |
| -------------- | ------------------- |
| 快速查找           | 是否存在某個值、是否重複        |
| 統計出現次數 / 配對條件  | 字元、數字、次數統計          |
| 空間換時間          | 預存所有出現過的資訊供 O(1) 查詢 |
| 支援非序列資料的組合或關聯性 | 分組、歸類、異位詞、和為某值的兩數   |

---

## 🎯 三、比喻理解：幫助你記憶與應用情境

| 題型                      | 比喻                         |
| ----------------------- | -------------------------- |
| Two Sum                 | 查手機聯絡人：「我缺 30 元，有沒有人剛好有」   |
| Group Anagrams          | 排同字母順序：就像把一樣食材的料理歸類        |
| Valid Anagram           | 兩個人買的菜單是否完全相同，不看順序         |
| Top K Frequent Elements | 看留言板最多人提到的詞，像統計熱搜關鍵字       |
| Subarray Sum Equals K   | 找總分剛好是 K 的小區段，像賽車中某段剛好配速完成 |

---

## 📚 四、Blind 75 中 Hash Table 題目清單

| 題目名稱                                           | 核心技巧                    |
| ---------------------------------------------- | ----------------------- |
| Two Sum                                        | 補數查找                    |
| Group Anagrams                                 | 排序 + Map 分組             |
| Valid Anagram                                  | 計數比對                    |
| Top K Frequent Elements                        | 頻率 Map + Heap（優先佇列）     |
| Subarray Sum Equals K                          | 前綴和 + Map               |
| Longest Substring Without Repeating Characters | 滑動窗 + Set / Map         |
| Contains Duplicate                             | Set 判重                  |
| LRU Cache                                      | 雙向 LinkedList + HashMap |

---

## ✏️ 五、每題簡單說明與策略

---

### 🔹 Two Sum

* **目標**：找出兩數之和為 target 的索引
* **策略**：建 hash map 儲存數值 → 搜尋 target - nums\[i]
* **時間複雜度**：O(n)

```ts
const map = new Map();
for (let i = 0; i < nums.length; i++) {
  const complement = target - nums[i];
  if (map.has(complement)) return [map.get(complement), i];
  map.set(nums[i], i);
}
```

---

### 🔹 Valid Anagram

* **目標**：判斷 s 和 t 是否為異位詞（Anagram）
* **策略**：使用字元計數 Map 或排序後比對

---

### 🔹 Group Anagrams

* **目標**：將所有異位詞放進同一群組
* **策略**：排序字串為 key，Map value 為陣列

---

### 🔹 Top K Frequent Elements

* **目標**：找出出現次數最多的前 K 個元素
* **策略**：用 Map 記錄頻率，再用 Heap 選出前 K 項

---

### 🔹 Subarray Sum Equals K

* **目標**：找出總和為 K 的連續子陣列數量
* **策略**：Prefix Sum + Map 記錄 sum 出現次數
* **核心公式**：若 `prefixSum[j] - prefixSum[i] = K`，則 i\~j 為合法區段

---

### 🔹 Longest Substring Without Repeating Characters

* **目標**：找出無重複字元的最長子字串長度
* **策略**：滑動窗 + Set / Map 儲存已見字元位置

---

### 🔹 Contains Duplicate

* **目標**：判斷是否有重複數字
* **策略**：用 Set 判重；若 Set 長度 ≠ 陣列長度，則有重複

---

### 🔹 LRU Cache

* **目標**：實作最近最少使用快取
* **策略**：雙向鏈結串列 + HashMap
* **需能做到**：O(1) 存取與刪除最近最少使用項目

---

## 🧩 六、常用模版（JavaScript / TypeScript）

### ✅ 查找補數（Two Sum）

```ts
const map = new Map();
for (let i = 0; i < nums.length; i++) {
  const need = target - nums[i];
  if (map.has(need)) return [map.get(need), i];
  map.set(nums[i], i);
}
```

---

### ✅ 字元頻率（Anagram）

```ts
const count = {};
for (let c of s) count[c] = (count[c] || 0) + 1;
for (let c of t) {
  if (!count[c]) return false;
  count[c]--;
}
```

---

### ✅ Prefix Sum + Map（Subarray Sum）

```ts
let map = new Map([[0, 1]]);
let sum = 0, count = 0;
for (let num of nums) {
  sum += num;
  if (map.has(sum - k)) count += map.get(sum - k);
  map.set(sum, (map.get(sum) || 0) + 1);
}
```

---

## ✅ 七、學習建議與記憶策略

| 建議                      | 原因與好處                     |
| ----------------------- | ------------------------- |
| 熟悉 Map / Set 使用 API     | 是解題效率與可讀性關鍵               |
| 記住常見操作模式（補數、統計、前綴）      | 降低思考負擔，遇到類題可馬上套用          |
| 把常見範例題做成模版              | 如：Two Sum, 字元計數、Group 類型題 |
| 分清「值存在」 vs「次數出現」        | 判斷題 vs 統計題需要不同策略          |
| 熟練 Map + Sliding Window | 字串、陣列題最常搭配                |



