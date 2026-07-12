class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] > target:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                break
        
        if l > r:
            return False
        
        col = (l + r) // 2

        l = 0
        r = n - 1

        while l <= r:
            col = (l+r) // 2
            
            if matrix[mid][col] == target:
                return True
            elif matrix[mid][col] < target:
                l = col + 1
            else:
                r = col - 1
        
        return False