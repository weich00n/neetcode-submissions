class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        n = len(s)

        check = [0] * 26

        for i in range(n):
            s_idx = ord(s[i]) - ord('a')
            t_idx = ord(t[i]) - ord('a')

            check[s_idx] += 1
            check[t_idx] -= 1
        
        for i in range(26):
            if check[i] != 0:
                return False
        
        return True