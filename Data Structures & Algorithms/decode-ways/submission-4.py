class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        #optimal structure
        #dp(i) = dp(i-1) -> before
        # += dp[i-2] if the thing before plus the guy is 10 - 26

        n = len(s)
        dp = [0] * (n+1)

        dp[0] = 1
        
        for i in range(1, n+1):
            if int(s[i-1]) != 0:
                dp[i] += dp[i-1]

            if i - 2 >= 0 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]