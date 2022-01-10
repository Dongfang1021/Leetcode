class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxRobbedAmount = [None for _ in range(len(nums)+1)]
        N = len(nums)
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]
        for i in range(N-2, -1, -1):
            maxRobbedAmount[i] = max(maxRobbedAmount[i+1], maxRobbedAmount[i+2]+ nums[i])
        return maxRobbedAmount[0]
        