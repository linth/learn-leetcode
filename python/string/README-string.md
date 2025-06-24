## LeetCode Blind 75：String 主題題目核心觀念

### 介紹

LeetCode Blind 75 中的 String（字串）主題涵蓋多種經典且實用的字串操作問題，包含字串搜尋、字元統計、字串匹配、回文判斷、字串分組等。這些題目不僅考察對字串資料結構的理解，也強調滑動視窗、雙指標、哈希表等技巧的應用，是面試中常見且重要的題型。

---

### 結論

練習 Blind 75 中的字串題目能幫助你：

- 熟悉字串的基本操作與常見技巧，如滑動視窗、雙指標、哈希映射。  
- 掌握如何有效處理字串中重複字元、子串匹配、回文判斷等問題。  
- 理解字串分組與排序的策略，提升對字串資料結構的敏感度。  
- 增強解決實際字串相關問題的能力，為面試做好準備。

---

### 比喻

把字串想像成一條由字母組成的「繩子」：

- **滑動視窗**就像用一個可移動的框框在繩子上滑動，尋找符合條件的子段。  
- **雙指標**像是兩隻手指從繩子的兩端往中間移動，快速定位特定區間。  
- **哈希表**則像是繩子上的標籤，幫助你快速記錄和查找字母出現的頻率或位置。  
- **回文**像是繩子從中間對折後，兩邊圖案完全對稱。

---

### 簡單說明

- **滑動視窗（Sliding Window）**：用於尋找符合條件的最長或最短子串，如「無重複字元的最長子串」。  
- **雙指標（Two Pointers）**：同時用兩個指標定位子串範圍，提升效率。  
- **哈希表（Hash Map）**：記錄字元出現次數，快速判斷字串特性，如異位詞分組。  
- **回文判斷**：判斷字串是否對稱，常用動態規劃或中心擴展法。  
- **經典題目舉例**：  
  - Longest Substring Without Repeating Characters（無重複字元的最長子串）  
  - Valid Anagram（有效的字母異位詞）  
  - Minimum Window Substring（最小覆蓋子串）  
  - Valid Parentheses（有效括號）  
  - Longest Palindromic Substring（最長回文子串）

---

> **總結：**  
> 字串題目是面試中高頻且實用的範疇，掌握滑動視窗、雙指標與哈希表等技巧，能讓你高效解決多種字串問題。將字串比喻為繩子與標籤，有助於理解操作過程與演算法思路，提升解題效率與信心。

---

此說明結合 Blind 75 字串題目特性與常見解題策略，幫助你快速掌握字串主題的核心觀念。

[1] https://www.reddit.com/r/csMajors/comments/1dxsdwu/blind75_vs_neetcode150/?tl=zh-hant \
[2] https://www.greatfrontend.com/zh-CN/interviews/blind75 \
[3] https://juejin.cn/post/7134304958144479269 \
[4] https://ithelp.ithome.com.tw/m/articles/10314475 \
[5] https://ithelp.ithome.com.tw/articles/10287061?sc=rss.qu \
[6] https://zyrastory.com/coding/blind75-list-and-solution/ \
[7] https://hackmd.io/@meyr543/HJvvgvjyq \
[8] https://www.youtube.com/watch?v=KzKVa5sBPjc \
[9] https://hackmd.io/@9o3XaP0iRyOF2-OGuqXoXQ/rkmzHA3U2 \
[10] https://vocus.cc/salon/cutesciuridae/room/leetcode75tutorial

---

針對 **LeetCode Blind 75 中與 String 主題相關題目** 的：

* 📘 主題介紹
* ✅ 解題結論
* 🎯 比喻類比
* ✏️ 每題簡單說明與策略

---

## 📘 一、主題介紹：什麼是 String 題？

String 題目通常包含以下幾種處理方向：

| 類型          | 說明              |
| ----------- | --------------- |
| 字元計數 / 比對   | 出現次數、異位詞、重組     |
| 子字串 / 子序列搜尋 | 最長、最短、匹配某條件的子字串 |
| 字串轉換 / 建構   | 翻轉、壓縮、格式化、重排    |
| 雙指針滑動窗      | 高效搜尋或組合子字串      |

String 題目雖簡單，但常是**高頻題型**，同時考驗：

* 對字串資料操作的熟悉程度
* 效率（`O(n)`）、空間（hash map / count array）
* 基礎演算法技巧（sliding window、prefix sum 等）

---

## ✅ 二、結論：掌握常見技巧，String 題會變得結構清晰！

| 技巧名稱                  | 常見用途            |
| --------------------- | --------------- |
| Sliding Window        | 找「最長/最短」滿足條件子字串 |
| HashMap / Count Array | 比較字元頻率（異位詞類型）   |
| 雙指針                   | 比對前後、反轉、壓縮等     |
| Substring + Map       | 找起點、計數、壓縮子字串    |

---

## 🎯 三、比喻類比：幫助你理解核心概念

| 題型                               | 比喻說明                   |
| -------------------------------- | ---------------------- |
| Valid Anagram                    | 比誰的購物清單內容一樣，不看順序       |
| Longest Substring Without Repeat | 滑動窗戶不讓房間內有重複人          |
| Group Anagrams                   | 把一樣字母組成的字排成同一組，就像整理抽屜  |
| Valid Palindrome                 | 檢查文字正著念、倒著念都一樣，有點像對稱圖形 |
| Encode and Decode Strings        | 把字串包裝再還原，就像壓縮與解壓縮過程    |

---

## 📚 四、Blind 75 中 String 題目列表

| 題目名稱                                           | 主題類型             | 技巧                   |
| ---------------------------------------------- | ---------------- | -------------------- |
| Valid Anagram                                  | 異位詞比對            | Count Map            |
| Group Anagrams                                 | 異位詞分組            | 排序 + Map             |
| Valid Palindrome                               | 是否為回文            | 雙指針                  |
| Longest Substring Without Repeating Characters | 最長無重複子字串         | Sliding Window       |
| Longest Palindromic Substring                  | 最長回文字串           | 中心擴展法                |
| Palindromic Substrings                         | 統計回文總數           | 中心擴展法                |
| Encode and Decode Strings                      | 字串序列化/反序列化       | 字串轉換                 |
| Implement strStr()                             | 字串查找             | 子字串比對                |
| Minimum Window Substring                       | 滑動窗找最短包含所有字元的子字串 | Sliding Window + Map |

---

## ✏️ 五、每題簡單說明與策略

---

### 🔹 Valid Anagram

* **目標**：s, t 是否為異位詞（anagram）
* **解法**：用 `hash map` 計數，看頻率是否完全一致
* **時間複雜度**：O(n)

---

### 🔹 Group Anagrams

* **目標**：把異位詞群組在一起
* **解法**：排序字串作為 key，Map 對應 List

```ts
map = {}
for word of words:
  sorted = ''.join(sorted(word))
  map[sorted].push(word)
```

---

### 🔹 Valid Palindrome

* **目標**：忽略非字母與大小寫，是否為回文？
* **解法**：雙指針 + isalnum 檢查

---

### 🔹 Longest Substring Without Repeating Characters

* **目標**：找出最長不重複子字串長度
* **技巧**：Sliding Window + Map 記錄字元位置
* **時間複雜度**：O(n)

---

### 🔹 Longest Palindromic Substring

* **目標**：找出最長回文子字串
* **技巧**：中心擴展（每個位置往左右擴展）

---

### 🔹 Palindromic Substrings

* **目標**：計算所有回文子字串數量
* **技巧**：中心擴展（每個字元為中心試擴展）

---

### 🔹 Encode and Decode Strings

* **目標**：將 list of strings 編碼為單一字串，再解碼還原
* **技巧**：加上長度編碼前綴，例如 `"5:apple4:book"`

---

### 🔹 Implement strStr()

* **目標**：找出 needle 在 haystack 的位置
* **技巧**：暴力比對、或 KMP（但通常暴力即可過）

---

### 🔹 Minimum Window Substring

* **目標**：找出最短子字串包含所有 target 字元
* **技巧**：Sliding Window + Map 記錄缺少的字元

---

## 🧩 六、常用技巧模版（JS / TS 可直接套）

---

### ✅ Sliding Window (最長不重複子字串)

```ts
let set = new Set();
let left = 0, right = 0, maxLen = 0;

while (right < s.length) {
  if (!set.has(s[right])) {
    set.add(s[right++]);
    maxLen = Math.max(maxLen, set.size);
  } else {
    set.delete(s[left++]);
  }
}
```

---

### ✅ Count Map (異位詞)

```ts
function isAnagram(s, t) {
  if (s.length !== t.length) return false;
  const count = {};
  for (let c of s) count[c] = (count[c] || 0) + 1;
  for (let c of t) {
    if (!count[c]) return false;
    count[c]--;
  }
  return true;
}
```

---

## ✅ 七、總結與建議

| 建議                   | 原因                                             |
| -------------------- | ---------------------------------------------- |
| 熟練 sliding window 模式 | 幾乎所有子字串類型題都會用到                                 |
| 了解 Map / Set 的使用     | 快速查找、比對、記錄位置                                   |
| 掌握中心擴展處理回文字串技巧       | 效率好又容易實作                                       |
| 練習處理空字串、大小寫、特殊符號     | 面試題常設陷阱                                        |
| 整理常見字串 API 使用技巧      | 如 `charCodeAt`, `substring`, `split`, `join` 等 |


