class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i=0
        while i<len(word1) and i<len(word2):
            res += word1[i] + word2[i]
            i += 1
        if i <len(word1):
            res += word1[i:]
        if i <len(word2):
            res += word2[i:]
        return res