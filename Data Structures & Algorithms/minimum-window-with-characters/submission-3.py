class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tMap = defaultdict(int)
        sMap = defaultdict(int)

        for c in t:
            tMap[c] += 1
        
        def check(tMap, sMap):
            for c in tMap:
                if tMap[c] > sMap[c]:
                    return False
            
            return True
        
        l = 0
        minLength = float('inf')
        minStart = 0

        for r in range(len(s)):
            # add r characther to window
            c = s[r]
            sMap[c] += 1

            # check valid window
            while l <= r and check(tMap, sMap):
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    minStart = l
                sMap[s[l]] -= 1
                l += 1
        
        return s[minStart:minStart+minLength] if minLength != float('inf') else ""






        