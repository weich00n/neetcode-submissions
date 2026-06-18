class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #dp[i] -> max profit
        # at each day you either buy or sell
        
        # if you buy u compare from 2 days ago
        #dp[i] = max(prices[i-1] - dp[i-2])
        # if you sell, you sell compared to your lowest price
        # only buy if more
        #dp[i] = max(prices[i-1] - min)
        n = len(prices)
        dp = [[0]*2 for _ in range(n + 1)]
        
        for i in range(n-1, -1, -1):
            
            # buying
            buy = dp[i+1][False] - prices[i] if i + 1 < n else - prices[i]
            cooldown = dp[i+1][True] if i + 1 < n else 0
            dp[i][1] = max(buy, cooldown)

            # selling
            sell = dp[i+2][True] + prices[i] if i + 2 < n else prices[i]
            cooldown = dp[i+1][False] if i + 1 < n else 0
            dp[i][0] = max(sell, cooldown)

        return dp[0][1]