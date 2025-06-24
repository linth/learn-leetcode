## LeetCode Blind 75：Stack 主題題目核心觀念

### 介紹

在 LeetCode Blind 75 題庫中，Stack（堆疊）雖然題目數量不多，但卻是非常重要的資料結構，常用於解決括號匹配、字串解析、單調棧等問題。堆疊遵循後進先出（LIFO）原則，適合處理需要暫存狀態並逆序處理的場景。

---

### 結論

熟悉 Stack 題目能讓你：

- 理解堆疊的基本操作：push（入棧）、pop（出棧）、peek（查看頂端元素）。  
- 掌握如何利用堆疊解決括號匹配、字串解析等問題。  
- 熟悉單調棧（Monotonic Stack）技巧，解決下一個更大元素、柱狀圖最大矩形等問題。  
- 理解堆疊在程式執行過程中如何管理函式呼叫與返回（如呼叫堆疊）。  
- 避免常見錯誤，如堆疊溢位（stack overflow）與空棧操作。

---

### 比喻

堆疊就像一疊盤子：

- 你只能從最上面拿取或放入盤子（後進先出）。  
- 當你放入新盤子時，是放在最上面（push）。  
- 當你拿盤子時，只能拿最上面的那個（pop）。  
- 你可以先看最上面的盤子是什麼（peek），但不拿走它。  
- 如果一直放入盤子卻不拿出來，盤子會越堆越高，最後可能會倒塌（stack overflow）。

---

### 簡單說明

- **基本操作**：  
  - **Push**：將元素放入堆疊頂端。  
  - **Pop**：移除並返回堆疊頂端元素。  
  - **Peek/Top**：查看堆疊頂端元素但不移除。  
- **典型題目**：  
  - Valid Parentheses（有效括號匹配）  
  - Min Stack（帶有取最小值功能的堆疊）  
  - Daily Temperatures（每日溫度，利用單調棧找下一個更高溫度）  
  - Largest Rectangle in Histogram（柱狀圖中最大矩形）  
- **時間複雜度**：大多數堆疊操作為 O(1)，整體題目多為 O(n)。  
- **應用場景**：括號匹配、函式呼叫管理、逆波蘭表示法計算、單調棧問題。

---

> **總結：**  
> Stack 是解決許多線性結構問題的利器，透過後進先出的特性，能有效管理暫存狀態與逆序操作。將堆疊比喻為一疊盤子，有助於理解其操作限制與應用場景，並避免常見錯誤。熟練堆疊題目，是面試中重要的基礎技能。

---

此說明結合 Blind 75 Stack 題目特性與常見解題策略，幫助你快速掌握核心觀念。

[1] https://neetcode.io/practice?tab=blind75 \
[2] https://takeuforward.org/interviews/blind-75-leetcode-problems-detailed-video-solutions \
[3] https://hackmd.io/@meyr543/HJvvgvjyq \
[4] https://leetcode.com/discuss/interview-question/4915703/my-solutions-to-blind-75 \
[5] https://www.youtube.com/watch?v=KzKVa5sBPjc \
[6] https://github.com/jaimin-bariya/blind-75-leetcode \
[7] https://www.reddit.com/r/leetcode/comments/xmxfms/blind_75_no_queue_or_stack/ \
[8] https://mohsentabibian.github.io/LeetCode-Solutions/15.%20Greedy/README.html \
[9] https://swiftrefresher.com/leetcode/blind-75-stack/

---

針對 **LeetCode Blind 75 中與 Stack 主題相關題目** 的：

---

## 📘 一、主題介紹：什麼是 Stack 題？

Stack（堆疊）是一種「先進後出」（**LIFO**）的資料結構，適合用來處理：

| 類型                    | 說明                         |
| --------------------- | -------------------------- |
| 括號 / 結構驗證             | 像是成對的符號或結構需要先進後出驗證         |
| 單調堆疊（Monotonic Stack） | 解決「找左邊/右邊最近大於或小於」這類問題      |
| 反轉控制流 / Undo          | 處理撤銷、回溯、還原等邏輯              |
| 遞迴改寫 / 模擬             | 用 stack 模擬 call stack 遞迴操作 |

---

## ✅ 二、結論：掌握 Stack，即掌握控制流程與狀態儲存的關鍵！

Stack 題目的共通點：

| 解題重點          | 解釋                        |
| ------------- | ------------------------- |
| 保留順序 / 狀態     | 如：括號比對、運算順序               |
| 處理「下一個更大/小元素」 | 單調堆疊技巧，搭配逆序遍歷更直覺          |
| 遞迴等價寫法或還原過程   | 需要保留中間狀態或多層流程時，Stack 特別好用 |

---

## 🎯 三、比喻與理解

| 題型                               | 生活比喻                  |
| -------------------------------- | --------------------- |
| Valid Parentheses                | 檢查括號是否成對關閉，就像推開的門要關上  |
| Min Stack                        | 像是疊盤子時，總是記得最小盤子在哪     |
| Evaluate Reverse Polish Notation | 逆波蘭計算器，像是操作工程計算機      |
| Daily Temperatures               | 問幾天後變熱，像看天氣預測資料堆起來再對照 |
| Car Fleet / Next Greater Element | 像排隊時觀察誰先走 / 誰擋在前面     |

---

## 📚 四、Blind 75 中 Stack 題目整理

| 題目名稱                             | 主題類型          | 技巧         |
| -------------------------------- | ------------- | ---------- |
| Valid Parentheses                | 括號成對驗證        | Stack 模擬   |
| Min Stack                        | 記錄最小值堆疊       | 輔助 stack   |
| Evaluate Reverse Polish Notation | 運算堆疊          | Stack 計算   |
| Daily Temperatures               | 單調遞減 stack    | 單調堆疊 + 遞減  |
| Car Fleet                        | 單調 stack 模擬車隊 | 倒序 + Stack |
| Next Greater Element I/II        | 單調遞減 stack    | 循環遍歷 + Map |

---

## ✏️ 五、每題簡單說明與策略

---

### 🔹 Valid Parentheses

* **目標**：確認 ()\[]{} 是否有正確開關
* **策略**：遇到開括號 push，遇到閉括號 pop 比對

```ts
const stack = [];
const map = { ')': '(', ']': '[', '}': '{' };
for (let c of s) {
  if (c in map) {
    if (stack.pop() !== map[c]) return false;
  } else {
    stack.push(c);
  }
}
return stack.length === 0;
```

---

### 🔹 Min Stack

* **目標**：實作 stack，但 `getMin()` 要 O(1)
* **策略**：額外用一個 stack 同步記錄目前最小值

---

### 🔹 Evaluate Reverse Polish Notation

* **目標**：給定逆波蘭表示法 (後序表示法)，求其值
* **策略**：遇數字 push，遇運算符就 pop 兩個做運算再 push

---

### 🔹 Daily Temperatures

* **目標**：對每一天，找出後面幾天會有更高溫
* **策略**：使用單調遞減 stack 儲存 index，從右往左遍歷

---

### 🔹 Car Fleet

* **目標**：計算幾台車能成為車隊（不會被超車）
* **策略**：從目標倒序走，記錄誰先到，誰會追到前車

---

### 🔹 Next Greater Element

* **目標**：對每個元素，找出右邊第一個比它大的值
* **策略**：單調遞減 stack 解決這種「右側比較」問題

---

## 🧩 六、常用模版

### ✅ Valid Parentheses

```ts
const map = { ')': '(', ']': '[', '}': '{' };
const stack = [];
for (let c of s) {
  if (map[c]) {
    if (stack.pop() !== map[c]) return false;
  } else {
    stack.push(c);
  }
}
return stack.length === 0;
```

---

### ✅ 單調 Stack（右邊第一個較大的值）

```ts
const res = Array(nums.length).fill(0);
const stack = [];
for (let i = nums.length - 1; i >= 0; i--) {
  while (stack.length && nums[stack[stack.length - 1]] <= nums[i]) {
    stack.pop();
  }
  res[i] = stack.length ? stack[stack.length - 1] : -1;
  stack.push(i);
}
```

---

## ✅ 七、總結與建議

| 建議項目                | 原因與收穫                    |
| ------------------- | ------------------------ |
| 練習「模擬流程」題（如括號、運算）   | Stack 幫你追蹤流程，考驗推進與還原順序   |
| 熟練單調 Stack 模式       | 很多題型都用這招：股票價格、溫度、元素比較等   |
| 學會倒序遍歷搭配 Stack      | 多數「向右看」題都會這樣搭配           |
| 使用輔助 Stack 儲存額外資訊   | 如 Min Stack 題，要記錄額外最小值   |
| 圖解思路流程，有助 Stack 題掌握 | Stack 最需要「推進→還原→對比」的圖解幫助 |



