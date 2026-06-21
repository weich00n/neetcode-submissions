class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        
        intervals.sort()

        prev = float('-inf')
        
        res = 0
        for i in range(len(intervals)):
            if intervals[i][0] < prev:
                res += 1
                prev = min(prev, intervals[i][1])
            else:
                prev = intervals[i][1]
        
        return res