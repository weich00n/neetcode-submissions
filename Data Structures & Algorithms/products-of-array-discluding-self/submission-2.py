class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        prefix = 1
        suffix = 1
        for i in range(1, n):
            prefix *= nums[i-1]
            ans[i] *= prefix

            suffix *= nums[n-i]
            ans[n-i-1] *= suffix

        return ans