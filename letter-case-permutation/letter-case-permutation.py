class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        return map("".join, itertools.product(*map(f, s)))
        
        