class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = []

        i = 0
        j = 0

        while i < len(word1) and j < len(word2):
            word3.append(word1[i])
            word3.append(word2[j])
            i += 1
            j += 1
        
        if i == len(word1):
            return "".join(word3) + word2[j:]
        else:
            return "".join(word3) + word1[i:]