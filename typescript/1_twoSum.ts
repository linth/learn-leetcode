/**
 * 1. two sum 
 * 
 * 🧩 題目簡述：
 * 給定一個整數陣列 nums 和一個目標值 target，請找出陣列中兩個數字，它們的總和等於 target，並回傳它們的 index（假設一定有解且不重複使用同一元素）。
 * 
 * 🧠 解題思路（譬喻 + 邏輯）：
 * 🎯 思考方式（譬喻）：
 * 想像你在逛夜市，目標是「湊出總共剛好 $100 元的兩樣商品」，你在走的時候會記住你看過哪些價錢的商品，然後問自己：
 * 「如果我現在看到 $60 的商品，那我需要另一個多少元的商品才能湊到 $100？答案是 $40。如果我之前有看過 $40，那就成功了！」
 * ➡️ 這個記住「看過什麼價錢」的動作，就是用 HashMap（Map） 來記錄。
 * 
 * ⏱ 時間與空間複雜度：
 * 時間複雜度：O(n) — 每個元素只看一次。
 * 空間複雜度：O(n) — 最壞情況要記住所有元素。
 * 
 * 
 * Reference:
 *  - https://leetcode.com/problems/two-sum/description/
 * 
 */

function TS_twoSum(nums: number[], target: number): number[] {
  const map = new Map<number, number>();

  for (let i=0; i<nums.length; i++) {
    const current = nums[i];
    const complement = target - current;

    if (map.has(complement)) {
      return [map.get(complement)!, i];
    }

    map.set(current, i);
  }
  throw new Error(`No solution found.`);
}


const res = TS_twoSum([2, 7, 11, 15], 9); 
console.log(res);

// Output: [0, 1]，因為 nums[0] + nums[1] = 2 + 7 = 9ㄋ
// 先把array的元素值一一去減掉target，放到map裡面，然後再確認是否存在map即可。
