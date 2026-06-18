class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        directions = [[0,1], [1,0], [-1,0], [0,-1]]

        memo = {}

        def dfs(r,c,prevVal):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or matrix[r][c] <= prevVal:
                return 0
            
            if (r,c) in memo:
                return memo[(r,c)]
                
            res = 1

            for dr,dc in directions:
                res = max(res, 1 + dfs(r+dr, c + dc, matrix[r][c]))
            
            memo[(r,c)] = res
            return res


        LIP = 0
        for i in range(ROWS):
            for j in range(COLS):
               LIP = max(LIP, dfs(i,j, float('-inf'))) 

        return LIP