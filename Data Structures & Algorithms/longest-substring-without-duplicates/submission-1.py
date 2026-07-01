class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        l = 0

        res = 0

        for r in range(len(s)):
            c = s[r]

            if c in map:
                l = max(l, map[c] + 1)

            map[c] = r
            res = max(res, r - l + 1)     

        return res