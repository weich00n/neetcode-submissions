class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        n = len(heights)

        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = heights[0]
        suffix[n-1] = heights[n-1]
        #[0, 0, 2, 2, 3, 3, 3, 3, 3, 3]
        #[3, 3, 3, 3, 3, 3, 3, 2, 1, 0]
        for i in range(1, n):
            prefix[i] = max(prefix[i-1], heights[i])
        
        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], heights[i])
        
        total = 0
        for i in range(n):
            total += min(prefix[i], suffix[i]) - heights[i]
            
        return total        

       
        