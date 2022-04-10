class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) + 1
        dp = [0]*n
        for i in range(2, n):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[n-1]