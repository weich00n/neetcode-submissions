class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # state dp(i,j) , if s[i] == s[j], and it is palindrome (dp(i-1, j+1))
        # if i,j not palindrome, then just carry on

        resIdx, resLen = 0, 0

        n = len(s)

        dp = [[False] * (n+1) for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1, -1, -1):
            for j in range(i,n):

                if s[i] == s[j]:
                    if j - i < 2 or dp[i+1][j-1] :
                        dp[i][j] = True
                        if resLen < (j-i+1):
                            resIdx = i
                            resLen = j - i + 1

        return s[resIdx: resIdx + resLen]