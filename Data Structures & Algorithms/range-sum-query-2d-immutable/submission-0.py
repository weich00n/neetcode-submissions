class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            prefix = 0
            for j in range(1, n+1):
                prefix += matrix[i-1][j-1]
                above = self.dp[i-1][j]
                self.dp[i][j] = prefix + above

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.dp[row2][col2]
        above = self.dp[row1-1][col2]
        left = self.dp[row2][col1 - 1]
        topLeft = self.dp[row1-1][col1-1]

        return bottomRight - above - left + topLeft
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)