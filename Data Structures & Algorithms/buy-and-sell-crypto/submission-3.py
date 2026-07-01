class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        lowest = float('inf')
        profit = 0

        for price in prices:
            profit = max(price - lowest, profit)    

            if price < lowest:
                lowest = price
        
        return profit