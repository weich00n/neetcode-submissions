class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()

        # compare the first and last because they are all common
        
        i = 0
        j = 0

        res = []

        while i < len(strs[0]) and j < len(strs[-1]) and strs[0][i] == strs[-1][j]:
            res.append(strs[0][i])
            i += 1
            j += 1
        
        return "".join(res)