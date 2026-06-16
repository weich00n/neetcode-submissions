class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # optimal substructure 

        # if word[i] = s[i + len(word[j])], dp[i] = dp[i + len(word[j])] 
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True

        for i in range(n-1, -1, -1):
            for word in wordDict:
                length = len(word)
                if i + length <= n and s[i:i+length] == word:
                    dp[i] = dp[i] or dp[i+length]
        
        return dp[0] 
