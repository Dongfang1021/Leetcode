class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        response, left, right = float('-inf'), 0, len(nums) - 1
        nums.sort()
        while left < right:
            total = nums[left] + nums[right]
            if total < k:
                response = max(response, total)
                left += 1
            else:
                right -= 1
        return -1 if response == float('-inf') else response
