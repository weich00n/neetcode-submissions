class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #   c r a b t
        # c 1 1 1 1 1
        # a 1 1 2 2 2
        # t 1 1 2 2 3
        #
        # if i == j, then dp[i][j] = 1 + max(dp[i-1][j] or dp[i][j-1]

        m = len(text1)
        n = len(text2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]