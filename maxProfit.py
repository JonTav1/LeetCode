class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        index = len(prices) - 1
        
        for i in range(len(prices)):
            if max_profit < max(prices[i:]) - prices[i]:
                max_profit = max(prices[i:]) - prices[i]
        return max_profit

