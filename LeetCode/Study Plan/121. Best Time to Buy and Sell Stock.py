class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        
        for index in range (1, len(prices)):
            profit = prices[index] - buy_price
            
            if profit > max_profit :
                max_profit = profit
                
            if prices[index] < buy_price:
                buy_price = prices[index]
        
        return max_profit
        
# Time complexity O(N)
# Space complexity O(1)
