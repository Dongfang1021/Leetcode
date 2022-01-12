class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums, target, k):
            res = []
            if len(nums) == 0 or nums[0]*k > target or nums[-1]*k < target:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i-1]:
                    for idx, set in enumerate(kSum(nums[i+1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)
            return res
        def twoSum(nums, target):
            res = []
            left = 0
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum < target or (left > 0 and nums[left] == nums[left - 1]):
                    left += 1
                elif sum > target or (right < len(nums) - 1 and nums[right] == nums[right + 1]):
                    right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
            return res
        nums.sort()
        return kSum(nums, target, 4)
        
