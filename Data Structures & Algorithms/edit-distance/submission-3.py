class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # optimal substructure
        # dp(i,j) represents minimum
        # dp(i,j) -> if i == j: dp(i-1)(j-1)
        # else: 1 operation + min(dp(i-1)(j), dp(i-1)(j-1), dp(i)(j-1))
        # delete, replace, or add

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