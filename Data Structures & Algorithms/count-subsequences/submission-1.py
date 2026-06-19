class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        

        l1 = len(s)
        l2 = len(t)

        if l2 > l1:
            return 0

        dp = [[0] * (l2+1) for _ in range(l1 + 1)]

        for i in range(l1+1):
            dp[i][l2] = 1


        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                dp[i][j] += dp[i+1][j]

                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        
        return dp[0][0]

       