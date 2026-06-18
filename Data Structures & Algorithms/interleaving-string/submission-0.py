class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 + n2 != n3:
            return False
        
        dp = {}

        def dfs(i,j):
            if i == n1 and j == n2:
                return True

            if (i,j) in dp:
                return dp[(i,j)]
            
            if i < n1 and s3[i+j] == s1[i] and dfs(i+1,j):
                return True
            if j < n2 and s3[i+j] == s2[j] and dfs(i, j+1):
                return True

            dp[(i,j)] = False
            
            return False
        
        return dfs(0,0)