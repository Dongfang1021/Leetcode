class Solution:
    def decodeString(self, s: str) -> str:
        res, _ = self.dfs(s, 0)
        return res
    def dfs(self, s, i):
        res = ''
        while i < len(s) and s[i] != ']':
            if s[i].isdigit():
                times = 0
                while i < len(s) and s[i].isdigit():
                    times = times*10 + int(s[i])
                    i += 1
                i += 1
                decodeString, i = self.dfs(s, i)
                i += 1
                res += times*decodeString
            else:
                res += s[i]
                i += 1
        return res, i
        