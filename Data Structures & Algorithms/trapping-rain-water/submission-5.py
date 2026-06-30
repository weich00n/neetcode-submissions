class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        n = len(heights)
        leftMax = heights[0]
        rightMax = heights[n-1]

        l = 0
        r = n - 1
        vol = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, heights[l])
                vol += leftMax - heights[l]
            else:
                r -= 1
                rightMax = max(rightMax, heights[r])
                vol += rightMax - heights[r]
        
        return vol

       
        