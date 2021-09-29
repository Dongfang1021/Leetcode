class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        
        def strToTuple(word):
            if len(word) > 1:
                lst = []
                for x in range(len(word) - 1):
                    diff = ord(word[x]) - ord(word[x+1])
                    if diff < 0:
                        diff = diff + 26
                    lst.append(diff)
                return tuple(lst)
            else:
                return 1
        for word in strings:
            output[strToTuple(word)].append(word)
        return [output[x] for x in output]