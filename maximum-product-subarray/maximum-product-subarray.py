class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        maximum = minimum = result = nums[0]
        for i in range(1, len(nums)):
            maximum, minimum = max(maximum*nums[i], minimum*nums[i], nums[i]), \
                                min(maximum*nums[i], minimum*nums[i], nums[i])
            result = max(result, maximum)
        return result