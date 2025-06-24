## LeetCode Blind 75：Queue 主題題目核心觀念

### 介紹

LeetCode Blind 75 是一份由業界資深工程師精選、涵蓋最常見面試題型的題庫，其中「queue（佇列）」主題涵蓋了多道經典問題，強調資料結構在實務運算中的應用。這些題目不只考你佇列的基本操作，更常結合 BFS（廣度優先搜尋）、滑動視窗（sliding window）、多執行緒等進階技巧，是面試中不可或缺的考點[1][2][4]。

---

### 結論

Blind 75 中與 queue 相關的題目，能幫助你：
- 熟悉佇列（queue）與雙端佇列（deque）的基本操作與應用場景。
- 理解 BFS 演算法在圖、樹、網格等結構中的實作方式。
- 掌握滑動視窗技巧，解決連續區間、最大/最小值等問題。
- 增強對資料流動與同步處理的理解，應對多種面試實戰題。

---

### 比喻

你可以把 queue 想像成「排隊買票」的隊伍：
- **先進先出（FIFO）**：最早排隊的人最先買到票，後來的人只能等前面的人處理完。
- **滑動視窗**就像一扇移動的窗戶，觀察隊伍中一段連續的人數變化。
- **雙端佇列（deque）**則像是兩頭都能進出的人潮通道，靈活調度。

---

### 簡單說明

- **Queue 題型常見應用：**
  - **BFS**：用佇列分層遍歷圖或樹，找最短路徑、層級關係等。
  - **滑動視窗**：用 deque 維護區間最大/最小值，解決如「最大滑動視窗」等題目。
  - **多執行緒/生產者消費者**：用 queue 緩衝資料流，確保資料有序處理。
- **常見題目舉例：**
  - Binary Tree Level Order Traversal（二元樹層序遍歷）
  - Number of Islands（島嶼數量，BFS 解法）
  - Sliding Window Maximum（最大滑動視窗）
- **解題技巧：**
  - 理解 queue 的基本操作（enqueue、dequeue）。
  - 熟悉 BFS 的流程，會用 queue 維護待處理節點。
  - 遇到區間問題時，思考是否能用 deque 優化效率。

---

> **總結：**  
> Queue 題目重在資料流動與分層處理的能力，就像排隊一樣，誰先來誰先服務。掌握 queue 與 deque，不僅能解決 BFS、滑動視窗等經典題，更能訓練你對資料結構與演算法的直覺，是面試必備的核心技能[1][2][4]。


---

針對 **LeetCode Blind 75 中與 Queue 主題相關題目** 的：

* 📘 **主題介紹**
* ✅ **結論歸納**
* 🧠 **生活比喻**
* ✏️ **簡單說明**

快速理解「Queue」在各種題型中的核心應用方式。

---

## 🧭 Queue 題目總覽（LeetCode Blind 75 中）

| 題號 | 題目名稱                              | 主題類型                    |
| -- | --------------------------------- | ----------------------- |
| 1  | Binary Tree Level Order Traversal | BFS traversal（典型 queue） |
| 2  | Implement Queue using Stacks      | 資料結構設計題                 |
| 3  | Rotting Oranges                   | 多源 BFS（2D grid + queue） |
| 4  | Number of Islands                 | BFS/DFS 可選（queue 為其中一種） |
| 5  | Clone Graph                       | BFS/DFS 皆可，常見 BFS queue |
| 6  | Course Schedule                   | 拓撲排序（Topological Sort）  |
| 7  | Pacific Atlantic Water Flow       | 雙向 BFS queue（變化型）       |

---

## ✅ 結論歸納：Queue 是「分層、最短距離、廣度遍歷」的最佳工具

| 類別         | 使用 Queue 的原因                        |
| ---------- | ----------------------------------- |
| BFS 遍歷     | 避免遞迴爆棧，適合處理「一層一層處理節點」的邏輯            |
| 網格型題目      | 處理 2D 地圖的多點擴散（如爛橘子、洪水）時，queue 是自然解  |
| 拓撲排序（依賴關係） | 找出處理順序，queue 可以儲存 in-degree = 0 的節點 |
| 模擬真實 queue | 用兩個 stack 實作 queue，常見資料結構設計題        |

---

## 🎨 比喻理解：Queue 就像排隊一樣

* **先來先處理**：就像排隊領便當，一層一層進行
* **BFS 是多層樓電梯**：你處理完第 n 層，queue 裡的就是第 n+1 層的節點
* **Rotting Oranges 像病毒傳染**：一圈圈往外擴張，每次處理一層 queue

---

## 🔍 題目重點解析（含簡單解釋）

---

### 1️⃣ Binary Tree Level Order Traversal

* **用途**：BFS 走訪每一層的節點
* **技巧**：Queue 先放 root，之後每層把左右子節點加入 queue
* **關鍵**：每輪 queue 長度代表當層節點數，for loop 處理該層
* **比喻**：一群人一層樓上電梯，下一層再上一群人

---

### 2️⃣ Implement Queue using Stacks

* **用途**：使用兩個 stack 實作 queue（面試常考）
* **技巧**：一個 stack 作為輸入、另一個作為輸出，必要時倒資料
* **比喻**：用兩個盒子模擬「進 → 倒 → 出」

---

### 3️⃣ Rotting Oranges

* **用途**：多源 BFS，處理爛橘子擴散的最短時間
* **技巧**：

  * 一開始把所有爛橘子放進 queue
  * 每輪處理 queue 中所有節點，並將新的腐爛橘子加入 queue
* **比喻**：像病毒傳播，傳染範圍每分鐘擴散一圈

---

### 4️⃣ Number of Islands（BFS 解法）

* **用途**：計算 2D grid 中有幾個獨立陸地塊
* **技巧**：從每個未拜訪的陸地開始 BFS，把整塊區域標記為拜訪
* **比喻**：每次看到新陸地就用 queue 擴展該區域，直到整塊處理完畢

---

### 5️⃣ Clone Graph

* **用途**：複製整張圖（無向圖）
* **技巧**：用 BFS 搭配 queue 處理所有節點與相鄰節點
* **比喻**：像是從一個點出發複製整張社交網路的關係圖

---

### 6️⃣ Course Schedule（Topological Sort）

* **用途**：判斷是否可以完成所有課程（無循環）
* **技巧**：

  * 使用 queue 存所有 in-degree = 0 的節點
  * 每次取出一個課程 → 更新相鄰節點的 in-degree
* **比喻**：要先修完前置課程才能修進階課 → queue 負責「排隊修課」

---

### 7️⃣ Pacific Atlantic Water Flow

* **用途**：找所有能流向兩個海洋的節點
* **技巧**：從 Pacific / Atlantic 同時做 BFS，記錄可達點，最後取交集
* **比喻**：水從海邊倒灌回山上，看哪些點能「同時流」向兩個方向

---

## 🧠 解法模式總結

| 題型                   | 解法模式                   | 補充                  |
| -------------------- | ---------------------- | ------------------- |
| Tree Level Traversal | 標準 BFS，用 queue 一層一層走   | 每層記錄 queue 長度       |
| 多源擴散（橘子、洪水）          | 初始點加入 queue，層層擴散       | 適合找擴散時間或最短距離        |
| 拓撲排序                 | queue 儲存 in-degree = 0 | 常見於依賴關係處理           |
| Graph clone / 拓展     | BFS queue 或 DFS        | 注意避免重複處理            |
| 資料結構模擬               | stack 實作 queue         | Stack/Queue 的互相模擬考點 |

---

## 🧰 學習建議

1. **熟練 BFS 模板**（queue 處理節點 → 擴展 → 加入 queue）
2. **掌握層級走訪邏輯（queue 長度代表層級）**
3. **練習 grid + BFS 模板題（Rotting Oranges, Islands）**
4. **理解 Topological Sort 的 queue + in-degree 機制**
5. **能用口語解釋 queue 的意義（如傳染、分層、排隊）**

---

需要我幫你整理出這些題目的 **程式碼模板、口語講解稿或精簡記憶法筆記** 嗎？也可以做成一張對照表或面試用速查 PDF！只要說一聲就行。
