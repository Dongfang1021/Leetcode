class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0 
        for cookie in s:
            if i >= len(g):
                return i
            if cookie >= g[i]:
                i += 1
        return i
