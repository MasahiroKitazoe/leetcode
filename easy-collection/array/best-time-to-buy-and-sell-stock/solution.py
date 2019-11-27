# runtime beats 42.6%
# memory usage beats under 5%

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = i = 0
        buy = None
        while i+1 < len(prices):
            if prices[i] > prices[i+1]:
                if buy is not None:
                    profit += prices[i] - buy
                    buy = None
            elif prices[i] < prices[i+1]:
                if buy is None:
                    buy = prices[i]
            i += 1
        if buy is not None:
            profit += prices[-1] - buy
        return profit

