class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # optimal substructure
        # dp(i,j) represents minimum
        # dp(i,j) -> if i == j: dp(i-1)(j-1)
        # else: 1 operation + min(dp(i-1)(j), dp(i-1)(j-1), dp(i)(j-1))
        # delete, replace, or add

        #base case, 0 for j, you need i deletions
        # base case, 0 for i, u need j insertions
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0] * (l2+1) for _ in range(l1+1)]

        for i in range(l1+1):
            dp[i][0] = i
        for j in range(l2+1):
            dp[0][j] = j
        
        for i in range(1, l1 + 1):
            for j in range(1, l2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
        
        return dp[l1][l2]



        l1 = len(word1)
        l2 = len(word2)

        memo = {}

        def dfs(i,j):
            # u reached the end of the word
            if i == l1:
                # u still have l2 - j to add
                return l2 - j  
            
            if j == l2:
                # you stil have l1 - i to delete
                return l1 - i
            
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i] == word2[j]:
                memo[(i,j)] = dfs(i+1, j+1)
            else:
                memo[(i,j)] = 1 + min(dfs(i+1, j+1), dfs(i,j+1), dfs(i+1,j))
            
            return memo[(i,j)]
        return dfs(0,0)