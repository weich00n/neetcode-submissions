class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False
        
        total = total // 2

        n = len(nums)

        dp = [[False] * (total+1) for _ in range(n+1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(total + 1):
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]] 
        
        return dp[n][total]
