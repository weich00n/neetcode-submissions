class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        l1 = len(s)
        l2 = len(t)

        if l2 > l1:
            return 0
        
        memo = {}

        def dfs(i,j):
            if j == l2:
                return 1
            
            if i >=  l1:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]

            res = dfs(i+1,j)

            if s[i] == t[j]:
                res += dfs(i+1, j+1)
            
            memo[(i,j)] = res
            return res

        return dfs(0,0)