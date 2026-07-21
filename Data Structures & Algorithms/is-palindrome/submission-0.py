class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def isalnum(c):
            return 'a' <= c <= 'z' or "A" <= c <= "Z" or "0" <= c <= "9";
        
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not isalnum(s[l]):
                l += 1

            while l < r and not isalnum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            r -= 1
            l += 1
        
        return True
            