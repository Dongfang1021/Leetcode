class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        memo = {}       
        def dfs(n, m):
            if n == m: return 1
            if n == 0 or m == 0: return 0
            n, m  = min(n,m), max(n, m)
            if n == 1: return m
            if m // n > 1:     #  This will reduce the recursion for  cases like (2, 11), (2, 9), ...,  to (2, 3) in one step
                return dfs(n, m % n + n) + m // n - 1
            if (n, m) in memo: return memo[(n, m)]
            res = dfs(m - n, n) + 1
            for s in range(n-1, m - n, -1):
                a = m - s
                b = n - s
                for k in range(b, a + 1):
                    recB = dfs(b, m - k)
                    recC = dfs(k - b, a - k)
                    recA = dfs(n - k, a)
                    ans = 2 + recB + recC + recA
                    res = min(res,ans)
            memo[(n, m)] = res
            return res
        return dfs(n, m)