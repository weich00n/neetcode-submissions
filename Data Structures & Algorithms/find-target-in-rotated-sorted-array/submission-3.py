class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        #find the min then split into two arrays to binary search from

        while l < r:
            mid = (l+r) // 2

            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid
        
        #check which partition target is in
        if nums[l] <= target <= nums[-1]:
            r = len(nums) - 1
        else:
            r = l - 1
            l = 0
        
        while l < r:
            mid = (l+r) // 2

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return l if nums[l] == target else -1
            
        
