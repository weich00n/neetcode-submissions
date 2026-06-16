class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        visit =  set()
        minHeap = [[grid[0][0], 0, 0]] # (time, row, col)
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        visit.add((0,0))

        while minHeap:
            maxLength, r, c = heapq.heappop(minHeap)

            if r == n-1 and c == n-1:
                return maxLength
            

            for dr, dc in directions:
                if 0 <= r + dr < n and 0 <= c + dc < n and (r + dr, c+dc) not in visit:
                    visit.add((r+dr, c+dc))
                    heapq.heappush(minHeap, [max(maxLength, grid[r+dr][c + dc]), dr + r, dc + c])





