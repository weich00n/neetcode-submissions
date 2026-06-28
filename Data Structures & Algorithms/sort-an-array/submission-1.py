
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        heapq.heapify(nums)
        for i in range(n):
            res.append(heapq.heappop(nums))
        
        return res

