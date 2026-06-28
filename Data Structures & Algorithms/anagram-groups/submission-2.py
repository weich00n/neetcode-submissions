class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for word in strs:
            check = [0] * 26
            for c in word:
                check[ord(c) - ord('a')] += 1
            
            res[tuple(check)].append(word)
        
        return list(res.values())