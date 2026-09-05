class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        currMin = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < currMin:
                currMin = prices[i]

            res = max(res, prices[i] - currMin)
        
        return res
