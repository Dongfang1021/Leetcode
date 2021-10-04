class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        if (target not in range(-1*totalSum, totalSum + 1)): return 0
        dp = [[0 for j in range(totalSum*2 + 1)] for i in range(len(nums))]
        dp[0][totalSum + nums[0]] += 1
        dp[0][totalSum - nums[0]] += 1
        for i in range(1, len(nums)):
            for j in range(totalSum*2 + 1):
                if (j - nums[i] >= 0 and dp[i - 1][j - nums[i]] > 0):
                    dp[i][j] += dp[i-1][j-nums[i]]
                if (j + nums[i] <= totalSum*2 and dp[i - 1][j + nums[i]] > 0):
                    dp[i][j] += dp[i - 1][j + nums[i]]
        return dp[-1][totalSum + target]