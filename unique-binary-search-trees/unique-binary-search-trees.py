class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 2:
            return n
        sol = [0]*(n+1)
        sol[0] = sol[1] = 1
        for i in range(2, n+1):
            for left in range(0, i):
                sol[i] += sol[left]*sol[i-1-left]
        return sol[n]