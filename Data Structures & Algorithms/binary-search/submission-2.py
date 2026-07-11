class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # F F T T
        # F F F F
        # F F T T
        # 1 3 5 6
        
        # 4 should return
        #l = 3
        # r = 5
        # 4 == -1

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return l if nums[l] == target else -1