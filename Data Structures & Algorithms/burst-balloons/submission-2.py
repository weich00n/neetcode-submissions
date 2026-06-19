class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # subproblem, what if i pop last, but then i count the subarray maximums        
        # dp(l,r) -> maxk -> dp(l,k-1), nums[l-1] * balloons[k] * nums[r+1]  , dp(k+1,r)
        
        nums = [1] + nums + [1]

        memo = {}

        def dfs(l,r):
            
            if l > r:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]

            memo[(l,r)] = 0
            for k in range(l, r+1):
                memo[(l,r)] = max(dfs(l, k-1) + dfs(k+1,r) + nums[l-1] * nums[k] * nums[r+1], memo[(l,r)])
            
            return memo[(l,r)]
        
        return dfs(1, len(nums)-2)