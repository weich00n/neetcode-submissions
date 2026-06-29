class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def dfs(i, bought):
            if i == len(prices):
                return 0
            
            if (i, bought) in memo:
                return memo[(i, bought)]
            res = dfs(i+1, bought)

            # either sell 
            if bought:
                res = max(res, prices[i] + dfs(i+1, False))
            
            # u buy now, then sell in the future
            else:
                res = max(res, -prices[i] + dfs(i+1, True))
            
            memo[(i,bought)] = res
            return res
            
        return dfs(0, False)

