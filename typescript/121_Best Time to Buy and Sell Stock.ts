/**
 * 121. Best Time to Buy and Sell Stock
 * 
 * 
 * 
 * Example 1:
 * Input: prices = [7,1,5,3,6,4]
 * Output: 5
 * Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
 * Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
 */

function TS_maxProfit(prices: number[]): number {
  let minPrice = Infinity;
  let max_profit = 0;

  for (const price of prices) {
    if (price < minPrice) {
      minPrice = price;
    } else {
      const profit = price - minPrice;

      if (profit > max_profit) {
        max_profit = profit;
      }
    }
  }
  return max_profit;
}

// 其實有點搞不懂，為什麼不需要考慮array的先後順 序？
{
  prices = [7,1,5,3,6,4];
  const result = TS_maxProfit(prices);

  console.log(result);
}
