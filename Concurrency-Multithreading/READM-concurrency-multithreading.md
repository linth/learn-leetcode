## LeetCode Blind 75：Concurrency / Multithreading 主題核心觀念

### 介紹

Concurrency（並發）與 Multithreading（多執行緒）是現代軟體開發中重要的技術，特別在需要同時處理多個任務、提升效能與資源利用率時。LeetCode Blind 75 中的相關題目涵蓋了執行緒同步、資源共享、死鎖預防、條件變數、鎖（locks）等核心概念，幫助你理解如何設計安全且高效的多執行緒程式。

---

### 結論

透過練習 Blind 75 的 Concurrency / Multithreading 題目，你將能：

- 理解執行緒的基本概念與生命週期。  
- 掌握同步機制（如鎖、信號量、條件變數）以避免競爭條件（race condition）與資料不一致。  
- 辨識並避免死鎖（deadlock）與活鎖問題。  
- 熟悉常見多執行緒問題的解法，如「Print in Order」、「Dining Philosophers」、「Bounded Blocking Queue」等。  
- 培養設計並發程式的思維，提升面試中解決系統設計與同步問題的能力。

---

### 比喻

可以把多執行緒想像成多個人在同一間廚房做菜：

- **執行緒（Thread）**是每個廚師，大家同時工作。  
- **鎖（Lock）**像是廚房裡的鍋子或爐台，當一個廚師在用時，其他人必須等候。  
- **同步（Synchronization）**確保廚師不會同時搶用同一個鍋子，避免食材混亂。  
- **死鎖（Deadlock）**就像兩個廚師各拿著一個鍋子，互相等待對方放下，結果誰也做不了菜。  
- **條件變數（Condition Variable）**像是廚師等水燒開的信號，收到通知才能繼續下一步。

---

### 簡單說明

- **Thread（執行緒）**：程式中可同時執行的最小單位。  
- **Synchronization（同步）**：控制多執行緒存取共享資源的機制，避免資料競爭。  
- **Locks（鎖）**：確保同一時間只有一個執行緒能操作特定資源。  
- **Condition Variables（條件變數）**：讓執行緒等待特定條件發生再繼續執行。  
- **Deadlock（死鎖）**：多個執行緒互相等待對方釋放資源，導致無限等待。  
- **常見題目**：  
  - Print in Order：多執行緒按順序輸出。  
  - Dining Philosophers：哲學家就餐問題，考慮資源分配與死鎖。  
  - Bounded Blocking Queue：實作有界阻塞佇列，控制生產者與消費者同步。  
  - Zero Even Odd：多執行緒交替輸出數字。

---

> **總結：**  
> Concurrency 與 Multithreading 題目考驗你對多執行緒間協調與同步的理解。掌握鎖、條件變數、死鎖預防等核心概念，並透過經典題目練習，能有效提升你設計安全且高效並發程式的能力，是面試中重要的技術競爭力。

---

此說明結合 LeetCode Blind 75 Concurrency / Multithreading 題目特性與關鍵概念，幫助你快速掌握核心觀念。

[1] https://leetcode.com/problem-list/concurrency/ \
[2] https://leetcode.com/problem-list/oizxjoit/ \
[3] https://www.scribd.com/document/521313511/Blind-75-Must-Do-Leetcode-Blind-75-Leetcode \
[4] https://neetcode.io/practice?tab=blind75 \
[5] https://www.youtube.com/watch?v=_o1BtzWIgi4 \
[6] https://stackoverflow.com/questions/72506328/concurrency-leetcode-problem-raise-a-time-limit-exceeded-without-any-understanda \
[7] https://www.youtube.com/watch?v=KzKVa5sBPjc \
[8] https://www.linkedin.com/posts/animeshchaudhri_httpserver-cplusplus-multithreading-activity-7189056162674180096-GAX5


---

針對 **LeetCode Blind 75 中與 Concurrency / Multithreading 主題** 的系統性整理，幫助你釐清觀念並理解面試常見題型。

---

## 📘 一、主題介紹：什麼是 Concurrency / Multithreading？

> **Concurrency** 指的是「任務可以交錯執行」
> **Multithreading** 是並發的一種實作方式，透過多個執行緒來並行處理程式邏輯。

常見的情境包括：

* 多個任務共享一個資源（例如印表機、資料庫）
* 任務間需要協調執行順序
* 確保程式在多執行緒下 **正確、安全、可預期**

---

## ✅ 二、結論：面試題的核心是「**同步控制與執行順序保障**」

| 類型                   | 重點               | 面試考點                                     |
| -------------------- | ---------------- | ---------------------------------------- |
| 順序執行控制               | 某任務 A 一定在任務 B 之前 | `lock`, `join`, `semaphore`              |
| 資源互斥 / 共享變數保護        | 多執行緒操作同一資料       | `mutex`, `atomic`, `volatile`            |
| 排程控制 / 任務限制          | 控制最大同時執行數、依賴順序   | `countdownLatch`, `barrier`, `semaphore` |
| 工具與語法（Java / Python） | 多執行緒語法與同步工具      | `synchronized`, `wait/notify`, `Event`   |

---

## 🎯 三、常見比喻

| 題型                  | 日常比喻              |
| ------------------- | ----------------- |
| 順序控制                | 你不能在炒菜前就盛盤        |
| 互斥鎖                 | 一次只能一個人使用洗衣機      |
| Semaphore 控制流量      | 電影院只有 3 個座位，超過就得等 |
| Barrier / Latch 同步點 | 要等所有人都到了才開始一起拍照   |

---

## 📚 四、Blind 75 中與 Concurrency 相關題目（擴充版）

雖然 Blind 75 沒有明確涵蓋這類題，但在 **FAANG 系列面試中非常常見**，以下是常考的題目：

| 題目名稱                                 | 說明與考點              |
| ------------------------------------ | ------------------ |
| Print FooBar Alternately (`FooBar`)  | **交替列印兩段文字**，需同步   |
| Print in Order (`Foo`, `Bar`, `Baz`) | **保證順序執行**三個函數     |
| H2O Generator                        | **控制執行緒數量與先後順序**   |
| FizzBuzz Multithreaded               | 多執行緒印出 FizzBuzz 結果 |
| Zero Even Odd                        | 三執行緒列印交錯的數字        |
| Dining Philosophers Problem          | 哲學家就餐問題，**死鎖預防**   |

---

## ✏️ 五、每題簡單說明與解法關鍵

---

### 🔹 Print in Order

* **目標**：三個方法（`first()`, `second()`, `third()`）必須照順序執行
* **解法**：

  * 使用 `Lock` + `Condition` 或 `Event`（Python）
  * Java 可使用 `CountDownLatch` 或 `Semaphore`

---

### 🔹 FooBar (Print FooBar Alternately)

* **目標**：`foo()` 和 `bar()` 各由一個執行緒負責，交錯列印 `foobarfoobar...`
* **技巧**：兩個執行緒間同步切換（用兩個信號量控制進入）

```python
from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_sem = Semaphore(1)
        self.bar_sem = Semaphore(0)

    def foo(self, printFoo):
        for _ in range(self.n):
            self.foo_sem.acquire()
            printFoo()
            self.bar_sem.release()

    def bar(self, printBar):
        for _ in range(self.n):
            self.bar_sem.acquire()
            printBar()
            self.foo_sem.release()
```

---

### 🔹 Zero Even Odd

* **目標**：由三個執行緒列印 0102030405...
* **技巧**：每個執行緒負責一種輸出，需設計執行順序控制
* **方法**：`Semaphore` 控制下一個要印誰

---

### 🔹 H2O Generator

* **目標**：3 個原子（2 氫 + 1 氧）要同步產生一個水分子
* **技巧**：`Semaphore` 控制最多兩個氫、一個氧進入，然後同步釋放

---

## 🧩 六、常用同步工具與概念

| 工具 / 概念           | 說明                        |
| ----------------- | ------------------------- |
| `Semaphore`       | 控制同時執行的最大執行緒數（例如 2H + 1O） |
| `Mutex / Lock`    | 確保某段程式碼同一時間只能一人執行         |
| `Event` (Python)  | 設置旗標讓執行緒等待 / 被喚醒          |
| `CountDownLatch`  | 等待所有任務完成後才繼續（Java）        |
| `Barrier`         | 多執行緒同時到達某一點後才一起繼續         |
| `Atomic Variable` | 保證單一變數的讀寫操作是不可分割的         |

---

## ✅ 七、學習與實作建議

| 建議                           | 說明                                                |
| ---------------------------- | ------------------------------------------------- |
| 熟悉 thread / lock / signal 工具 | Python: `threading`; Java: `synchronized`, `Lock` |
| 練習「順序控制」與「互斥控制」題型            | 題型簡單但邏輯難，極需理解與實作                                  |
| 學會 trace log 訊息 + 時間線        | 看輸出順序是否如預期執行                                      |
| 搭配 FAANG 行為面試準備說明機制          | 面試中需能清楚「口說」同步機制與為什麼這樣設計                           |



