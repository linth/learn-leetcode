## LeetCode Blind 75：Graph 主題題目核心觀念

### 介紹

LeetCode Blind 75 中的 Graph 主題包含多個中等到困難難度的經典問題，涵蓋圖的建構、遍歷、拓撲排序、環路檢測、最短路徑等重要概念。圖結構是面試中常見且重要的資料結構，能幫助你理解複雜關係網路與多重路徑問題，並掌握深度優先搜尋（DFS）、廣度優先搜尋（BFS）等演算法的應用。

---

### 結論

熟練 Blind 75 的 Graph 題目，能讓你：

- 掌握圖的表示法（鄰接表、鄰接矩陣）與建構技巧。  
- 熟悉 DFS 與 BFS 的實作與應用，解決遍歷與搜尋問題。  
- 理解拓撲排序的原理，用於有向無環圖（DAG）問題，如課程安排。  
- 能判斷圖中是否存在環路（cycle detection），避免無限循環。  
- 熟悉 Union-Find 結構，用於判斷連通性與環路檢測。  
- 提升解決複雜網路關係問題的能力。

---

### 比喻

你可以把圖想像成城市地圖：

- **節點（Node）**是城市中的各個地點。  
- **邊（Edge）**則是連接城市間的道路。  
- **DFS**就像是從一個地點出發，沿著路徑一直走到底，再回頭探索其他路徑。  
- **BFS**像是從起點出發，先拜訪所有相鄰地點，再逐層擴散到更遠的地點。  
- **拓撲排序**就像安排一場活動的流程，必須先完成某些步驟才能進行下一步。  
- **環路檢測**則是確認地圖中是否有繞圈的路徑，避免走回頭路。

---

### 簡單說明

- **圖的表示**：常用鄰接表儲存節點與其相鄰節點，節省空間。  
- **DFS 與 BFS**：DFS 適合深度探索，BFS 適合尋找最短路徑或層級遍歷。  
- **拓撲排序**：用於有向無環圖，確定節點的先後順序。  
- **環路檢測**：DFS 或 Union-Find 可用來判斷圖中是否存在環。  
- **經典題目**：Clone Graph（複製圖）、Course Schedule（課程安排）、Number of Connected Components（連通分量數）、Graph Valid Tree（判斷是否為樹）等。

---

> **總結：**  
> Graph 題目是程式面試中挑戰性較高的範疇，透過熟悉圖的結構與演算法，你能有效解決複雜關係網路與路徑問題。將圖比喻為城市地圖，有助於理解遍歷、排序與環路檢測的核心概念，提升解題直覺與效率。

---

此說明結合 Blind 75 Graph 題目特性與常見解題思維，幫助你快速掌握核心觀念。

[1] https://takeuforward.org/interviews/blind-75-leetcode-problems-detailed-video-solutions \
[2] https://neetcode.io/practice?tab=blind75 \
[3] https://www.youtube.com/watch?v=5QEitM6boaA \
[4] https://dev.to/educative/leetcode-blind-75-1e00 \
[5] https://www.youtube.com/watch?v=KzKVa5sBPjc \
[6] https://www.youtube.com/watch?v=d_8QZ0x9yTo \
[7] https://www.youtube.com/watch?v=PHTldlyo-Xc \
[8] https://grokkingtechinterview.com/blind-75-leetcode-explained-when-to-use-it-and-when-to-move-beyond-it-f3a7cb1f5346


---

針對 **LeetCode Blind 75 中與 Graph 主題相關題目** 的完整整理：

---

## 🧠 Graph 主題：介紹、結論、比喻、簡單說明

---

### 📘 一、主題介紹：什麼是 Graph？

Graph 是由「**節點（Node）**」與「**邊（Edge）**」構成的資料結構，常見於社交網路、地圖、課程先後關係、系統依賴圖等。

* 分為：

  * **有向圖 / 無向圖**
  * **帶權圖 / 無權圖**
  * **循環 / 非循環圖**

---

### ✅ 二、結論：Graph 題目的關鍵在於「遍歷」與「結構建模」

| 類型       | 方法                       | 關鍵工具與技巧               |
| -------- | ------------------------ | --------------------- |
| 遍歷與探索    | DFS / BFS                | visited, stack/queue  |
| 最短路徑     | BFS (無權圖) / Dijkstra（帶權） | queue + dist          |
| 圖合法性判斷   | 拓撲排序、Cycle Detection     | in-degree, visited 記錄 |
| 複製 / 連通性 | DFS + Map / Union-Find   | map clone, find-union |

---

### 🎯 三、Blind 75 中 Graph 題目總覽

| 題目名稱                        | 類型       | 方法               |
| --------------------------- | -------- | ---------------- |
| Clone Graph                 | 遍歷 + 複製  | DFS/BFS          |
| Number of Islands           | 圖中區塊遍歷   | DFS/BFS          |
| Course Schedule             | 拓撲排序     | BFS              |
| Graph Valid Tree            | Cycle 判斷 | DFS / Union-Find |
| Pacific Atlantic Water Flow | 多源遍歷     | DFS/BFS          |
| Word Ladder                 | 最短轉換路徑   | BFS + Graph 建模   |
| Word Search                 | 字元圖探索    | DFS + 回溯         |

---

### 🧠 四、核心觀念比喻

| 題型                | 日常比喻                 |
| ----------------- | -------------------- |
| Clone Graph       | 像是複製一張地圖，走到哪就畫到哪     |
| Course Schedule   | 像是修課計畫表，要先修哪些才能修後面課  |
| Number of Islands | 像用油漆桶工具把連在一起的區塊都標成一組 |
| Graph Valid Tree  | 檢查地圖是不是沒有回圈（像樹）且全連通  |
| Pacific Atlantic  | 看水能從哪個格子流到兩邊大海       |
| Word Ladder       | 找最短的字變換步驟組成新字        |

---

### ✏️ 五、每題簡單說明與邏輯策略

---

#### 🔹 Clone Graph

* **題意**：給一個無向圖的節點，請你深度複製這整個圖。
* **技巧**：用 `visited Map<Node, ClonedNode>` 避免無限遞迴。
* **方法**：DFS or BFS 都可，重點是邊走邊 clone。

---

#### 🔹 Number of Islands

* **題意**：二維網格中有多少個被水包圍的陸地塊？
* **技巧**：DFS/BFS 遍歷所有相連的陸地，把它們標記為 visited。
* **方法**：每次遇到「1」，就啟動一次遍歷 + 塗色。

---

#### 🔹 Course Schedule

* **題意**：有一堆課的前後依賴，能不能全部修完？
* **技巧**：拓撲排序判斷有無循環（如果有環就無法修完）
* **方法**：建圖 + 計算 in-degree，BFS 一層一層清除。

---

#### 🔹 Graph Valid Tree

* **題意**：這張圖是不是一棵合法的樹？
* **技巧**：樹的定義 = 無環 + 全連通
* **方法**：

  * DFS 檢查是否有 Cycle
  * 或用 Union-Find 合併判斷

---

#### 🔹 Pacific Atlantic Water Flow

* **題意**：哪個格子能同時流到太平洋和大西洋？
* **技巧**：**反向思考**：從海邊往回找「能流進」的格子
* **方法**：雙邊 DFS 標記 + 交集取格子

---

#### 🔹 Word Ladder

* **題意**：從 begin word 一步步換成 end word，最短需要幾步？
* **技巧**：

  * 每次只能改一個字母
  * 字典中的詞才有效
* **方法**：用 BFS 建立 word graph，逐層擴展（最短路徑）

---

#### 🔹 Word Search

* **題意**：從字元網格中找出某個單字
* **技巧**：每個格子當起點，走上下左右的 DFS
* **方法**：DFS + 回溯 + 使用 visited or in-place 修改

---

### 🧩 六、Graph 通用模板

---

#### ✅ DFS Template

```ts
function dfs(node) {
  if (!node || visited.has(node)) return;
  visited.add(node);
  for (const neighbor of node.neighbors) {
    dfs(neighbor);
  }
}
```

---

#### ✅ BFS Template

```ts
const queue = [start];
const visited = new Set([start]);

while (queue.length > 0) {
  const node = queue.shift();
  for (const neighbor of node.neighbors) {
    if (!visited.has(neighbor)) {
      visited.add(neighbor);
      queue.push(neighbor);
    }
  }
}
```

---

#### ✅ Topological Sort (Course Schedule)

```ts
const inDegree = new Map();
const graph = new Map();

// 建圖 + 計算 in-degree
for (...) {
  // 建立 graph 和 inDegree
}

const queue = [];
for (const node of graph) {
  if (inDegree.get(node) === 0) queue.push(node);
}

let count = 0;
while (queue.length > 0) {
  const node = queue.shift();
  count++;
  for (const neighbor of graph.get(node)) {
    inDegree.set(neighbor, inDegree.get(neighbor) - 1);
    if (inDegree.get(neighbor) === 0) {
      queue.push(neighbor);
    }
  }
}

return count === totalCourses;
```

---

## ✅ 學習建議總結

| 建議                       | 說明                              |
| ------------------------ | ------------------------------- |
| 熟悉建圖方式                   | adjacency list（Map）與 matrix 都要會 |
| DFS 與 BFS 模板都要會背         | 並知道什麼時候適合用哪個                    |
| 練習拓撲排序                   | 判斷 DAG 的核心技巧，與課程依賴常見            |
| 熟悉 visited 與 parent 跟蹤技巧 | 避免 Cycle 或幫助剪枝                  |
| 熟悉 Union-Find 用法         | 圖合併、Cycle 檢查、群組判斷時好用            |

