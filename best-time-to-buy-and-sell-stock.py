class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       profit = 0
       cp = prices[0]

       for price in prices[1:]:
            if cp > price:
                cp = price
            profit = max(profit, price - cp)
       return profit
