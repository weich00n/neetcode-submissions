class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # subproblem, what if i pop last, but then i count the subarray maximums        
        # dp(l,r) -> maxk -> dp(l,k-1), nums[l-1] * balloons[k] * nums[r+1]  , dp(k+1,r)
        
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * (n) for _ in range(n)]

        for length in range(1, n-1):
            for l in range(1, n-length):
                r = l + length - 1
                for k in range(l, r + 1):
                    dp[l][r] = max(dp[l][r], dp[l][k-1] + dp[k+1][r] + nums[l-1] * nums[k] * nums[r+1])
        
        return dp[1][n-2]

        