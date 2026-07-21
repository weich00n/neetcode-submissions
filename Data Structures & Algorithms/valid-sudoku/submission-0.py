class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        m,n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                num = board[i][j]
                if num in row[i] or num in col[j] or num in box[(i//3,j//3)]:
                    return False
                row[i].add(num)
                col[j].add(num)
                box[(i//3, j//3)].add(num)

        return True  