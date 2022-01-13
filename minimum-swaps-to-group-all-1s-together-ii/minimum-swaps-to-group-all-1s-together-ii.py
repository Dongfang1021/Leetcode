class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones, N = sum(nums), len(nums)
        min_swap = s = ones - sum(nums[:ones])
        for i in range(N):
            s += nums[i] - nums[(i + ones) % N]
            min_swap = min(s, min_swap)
        return min_swap