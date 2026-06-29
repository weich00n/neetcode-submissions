class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        square = defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.':
                    continue
                # cols
                if num in cols[j]:
                    return False
                cols[j].add(num)
                # rows
                if num in rows[i]:
                    return False
                rows[i].add(num)
                #square
                if num in square[(i//3, j//3)]:
                    return False
                square[(i//3,j//3)].add(num)
        
        return True