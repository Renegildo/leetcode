class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        l, r = 0, 1
        maxProfit = 0
        
        for i in range(len(prices)):
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
            
            if prices[r] < prices[l]:
                l = r
            
            if r < len(prices) - 1:
                r += 1
        
        return maxProfit