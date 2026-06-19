class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        m = len(s)
        n = len(p)

        dp = {}

        def dfs(i,j):
            if j == n:
                return i == len(s)

            if (i,j) in dp:
                return dp[(i,j)]

            match = i < m and (s[i] == p[j] or p[j] == '.')
            
            
            if j+1 < n and p[j+1] == '*':
                # don't use star
                dontUse = dfs(i, j+2)
                use = match and dfs(i+1, j)
                dp[(i,j)] = dontUse or use 
                return dp[(i,j)]

            if match:
                dp[(i,j)] = dfs(i+1, j+1)
                return dp[(i,j)]

            return False
        
        return dfs(0,0)
