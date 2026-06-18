class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums) + target

        if total % 2 == 1:
            return 0

        total //= 2
        n = len(nums)        
        #knapsack!
        dp = [[0] * (total+1) for _ in range(n+1)]

        dp[0][0] = 1

        for i in range(1, n+1):
            for j in range(total + 1):
                dp[i][j] = dp[i-1][j] 

                if j >= nums[i-1]:
                    dp[i][j] += dp[i-1][j-nums[i-1]]
        
        return dp[n][total]
        
        