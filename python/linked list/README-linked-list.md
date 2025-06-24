## LeetCode Blind 75：Linked List 主題題目核心觀念

### 介紹

Linked List（鏈結串列）是面試中常見的資料結構，Blind 75 中涵蓋多個經典題目，如反轉鏈結串列、合併排序鏈結串列、刪除倒數第 N 個節點、檢測環路等。這些題目考察你對鏈結串列節點操作、指標調整與空間時間複雜度的掌握。

---

### 結論

熟練鏈結串列題目，能讓你：

- 理解單向與雙向鏈結串列的結構與操作。  
- 掌握節點指標的調整技巧，如反轉鏈結串列時的指標反向。  
- 熟悉快慢指標技巧，用於檢測環路、找中點等問題。  
- 練習合併多個排序鏈結串列，理解如何以最小空間複雜度合併節點。  
- 增強對指標操作的直覺，避免常見錯誤如空指標存取。

---

### 比喻

你可以把鏈結串列想像成一串手鍊：

- 每個節點像是一顆珠子，珠子上有繩子連接下一顆珠子。  
- 反轉鏈結串列就像把手鍊反過來戴，繩子的方向要調整。  
- 快慢指標就像兩個人在手鍊上同時走，一個走得快，一個走得慢，用來找中間或檢查是否繞圈。  
- 合併鏈結串列像是把兩條手鍊按大小順序串成一條。

---

### 簡單說明

- **反轉鏈結串列**：利用三個指標（prev、curr、next）逐節點反轉指向。  
- **快慢指標**：兩個指標同時移動，快指標一次兩步，慢指標一次一步，用於找中點或偵測環路。  
- **合併兩個排序鏈結串列**：用雙指標比較節點大小，從頭建立新的排序鏈結串列。  
- **刪除倒數第N個節點**：利用快慢指標保持距離，定位目標節點並刪除。  
- **檢測環路**：快慢指標相遇表示有環。  
- **經典題目**：  
  - Reverse Linked List（反轉鏈結串列）  
  - Merge Two Sorted Lists（合併兩個排序鏈結串列）  
  - Remove Nth Node From End of List（刪除倒數第N個節點）  
  - Linked List Cycle（鏈結串列環路檢測）

---

> **總結：**  
> Linked List 題目重點在於指標操作與節點連結的靈活調整。熟悉快慢指標與反轉技巧，能幫助你解決多種鏈結串列問題。將鏈結串列比喻為串珠手鍊，有助於理解節點間的關係與操作流程，提升面試解題效率。

---

此說明結合 Blind 75 鏈結串列題目特性與解題思維，幫助你快速掌握核心觀念。

[1] https://neetcode.io/practice?tab=blind75 \
[2] https://www.youtube.com/watch?v=B3z32ehyDc0 \
[3] https://leetcode.com/problem-list/linked-list/ \
[4] https://www.techinterviewhandbook.org/best-practice-questions/ \
[5] https://dmytros.blog/posts/leetcode-blind-75-reverse-linked-list/ \
[6] https://takeuforward.org/interviews/blind-75-leetcode-problems-detailed-video-solutions \
[7] https://github.com/SwarajShelavale/LeetCode-Blind-75 \
[8] https://leetcode.com/discuss/general-discussion/460599/leetcode-solution-index/

---

針對 **LeetCode Blind 75 中與 Linked List 主題** 相關題目的：

* 📘 主題介紹
* ✅ 核心結論
* 🎯 比喻理解
* ✏️ 題目說明與解題策略

---

## 📘 一、主題介紹：什麼是 Linked List 題？

Linked List（鏈結串列）是一種線性資料結構，每個節點（Node）包含：

* 資料（value）
* 指向下一個節點的指標（`next`）

常見類型有：

* **Singly Linked List**（單向鏈結）
* **Doubly Linked List**（雙向）
* **Circular Linked List**（循環）

---

## ✅ 二、結論：Linked List 題目關鍵在於「指標操作與邊界處理」

| 技巧類型              | 說明                             |
| ----------------- | ------------------------------ |
| 雙指標技巧             | 快慢指標、prev/cur 控制節點關係           |
| 虛擬頭節點（Dummy Head） | 簡化插入/刪除操作，避免處理 head 特例         |
| 反轉鏈結              | 須小心 `prev`, `cur`, `next` 鏈接順序 |
| 環形檢測              | 使用快慢指標，找到是否有環、入環點              |
| 中點/倒數第 N 個        | 快慢指標的經典應用                      |

---

## 🎯 三、常見比喻說明

| 題型                        | 比喻                 |
| ------------------------- | ------------------ |
| 反轉 Linked List            | 倒帶錄影帶，把箭頭反過來       |
| 合併兩個 Linked List          | 像兩條火車併軌，依大小排列      |
| 環形偵測                      | 快慢跑者：一快一慢繞圈，若有環會相遇 |
| 移除倒數第 N 個節點               | 先讓快指標走 N 步，之後同步前進  |
| 判斷 Palindrome Linked List | 對折字串，看兩邊是否相同       |

---

## 📚 四、Blind 75 中 Linked List 題目列表

| 題目名稱                             | 類型        | 技巧重點              |
| -------------------------------- | --------- | ----------------- |
| Reverse Linked List              | 反轉        | 三指標反轉法            |
| Merge Two Sorted Lists           | 合併排序      | 遞迴 or 雙指針         |
| Linked List Cycle                | 是否成環      | 快慢指標              |
| Linked List Cycle II             | 找入環點      | Floyd 演算法         |
| Remove Nth Node From End of List | 刪除倒數第 N 個 | 快慢指針，+ Dummy Node |
| Reorder List                     | 鏈結重排      | 找中點 + 反轉 + 合併     |
| Palindrome Linked List           | 是否為回文     | 快慢指針 + 反轉一半       |

---

## ✏️ 五、每題簡單說明與策略

---

### 🔹 Reverse Linked List

* **目標**：將鏈結串列反轉
* **策略**：使用三個指標：`prev`, `curr`, `next`

```ts
let prev = null, curr = head;
while (curr) {
  let next = curr.next;
  curr.next = prev;
  prev = curr;
  curr = next;
}
return prev;
```

---

### 🔹 Merge Two Sorted Lists

* **目標**：合併兩個升序鏈結串列
* **策略**：遞迴或迴圈兩種解法，取小節點往下接
* **技巧**：可用 dummy head 簡化

---

### 🔹 Linked List Cycle

* **目標**：判斷是否有環
* **策略**：快慢指標（慢走一步，快走兩步），若有環必相遇

---

### 🔹 Linked List Cycle II

* **目標**：找到入環點
* **策略**：快慢指標相遇後，將其中一個移回頭，再同步前進，相遇即為入環點
* **公式**：`2a + 2b = a + b + c` 推得 `a = c`

---

### 🔹 Remove Nth Node From End of List

* **目標**：刪除倒數第 N 個節點
* **策略**：快指標先走 N 步，然後快慢同步走，當快指到尾時，慢指在要刪的位置前一個
* **技巧**：Dummy Node 避免刪 head 特例

---

### 🔹 Reorder List

* **目標**：重排鏈結串列成 L0 → Ln → L1 → Ln-1 → ...
* **策略**：找中點 → 反轉後半 → 合併兩段

---

### 🔹 Palindrome Linked List

* **目標**：判斷鏈結串列是否為回文
* **策略**：快慢指標找中點 → 反轉後半 → 比對前後兩段 → 還原（可選）

---

## 🧩 六、技巧模板整理

### ✅ 反轉鏈結串列模板

```ts
let prev = null;
let curr = head;

while (curr) {
  let next = curr.next;
  curr.next = prev;
  prev = curr;
  curr = next;
}
return prev;
```

---

### ✅ 快慢指針找中點

```ts
let slow = head, fast = head;
while (fast && fast.next) {
  slow = slow.next;
  fast = fast.next.next;
}
// slow 為中點
```

---

### ✅ 移除倒數第 N 個節點

```ts
let dummy = new ListNode(0);
dummy.next = head;
let fast = dummy, slow = dummy;
for (let i = 0; i <= n; i++) fast = fast.next;
while (fast) {
  fast = fast.next;
  slow = slow.next;
}
slow.next = slow.next.next;
return dummy.next;
```

---

## ✅ 七、學習建議與練習策略

| 建議                         | 說明              |
| -------------------------- | --------------- |
| 熟悉 Dummy Head 使用時機         | 避免刪除 head 的特殊處理 |
| 手寫指標交換過程（prev, curr, next） | 培養反轉時的思考流程      |
| 快慢指標應用場景清單記憶               | 找中點、找環、找倒數第 n 個 |
| 實作時善用圖解與紙筆模擬               | 幫助理解指標變化與節點位置移動 |
| 練習遞迴與迴圈兩種版本（如合併）           | 增強不同思路的靈活運用     |


