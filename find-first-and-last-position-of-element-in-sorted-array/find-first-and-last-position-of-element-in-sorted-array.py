class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]
        upper_bound = self.findBound(nums, target, False)
        return [lower_bound, upper_bound]
    
    def findBound(self, nums, target, isFirst):
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                if isFirst:
                    if pivot == left or nums[pivot - 1] < target:
                        return pivot
                    right = pivot - 1
                else:
                    if pivot == right or nums[pivot + 1] > target:
                        return pivot
                    left = pivot + 1
            elif nums[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1
        