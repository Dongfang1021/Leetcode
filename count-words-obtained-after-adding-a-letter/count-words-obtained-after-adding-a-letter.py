class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start_set = {"".join(sorted(w)) for w in startWords}
        count = 0
        for word in targetWords:
            if len(word) > 1:
                w = "".join(sorted(word))
                for i in range(len(word)):
                    if f"{w[:i]}{w[i+1:]}" in start_set:
                        count +=1
                        break
        return count
