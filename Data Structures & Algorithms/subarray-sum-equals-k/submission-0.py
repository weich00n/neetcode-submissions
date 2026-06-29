class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCount = {0:1}

        res = 0
        total = 0
        for num in nums:
            total += num
            diff = total - k

            
            res += prefixCount.get(diff, 0)
            prefixCount[total] = 1 + prefixCount.get(total, 0)
        
        return res

