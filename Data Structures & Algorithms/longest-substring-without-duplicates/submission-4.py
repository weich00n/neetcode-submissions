class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIndexMap = {}
        res = 0
        l = 0

        for r in range(len(s)):
            if s[r] in lastIndexMap:
                l = max(lastIndexMap[s[r]] + 1, l)

            lastIndexMap[s[r]] = r 
            res = max(r - l + 1, res)

        return res