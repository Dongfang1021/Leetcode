class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        j, current, max_ones = -1, 0, 0
        for i in range(0, len(nums)):
            if nums[i] == 1 or (nums[i] == 0 and j < 0):
                current += 1
            if current > max_ones:
                max_ones = current
            if nums[i] != 0:
                continue
            if j >= 0:
                current = i - j
            j = i
        return max_ones