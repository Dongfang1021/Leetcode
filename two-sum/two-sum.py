class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        for num_index, num in enumerate(nums):
            if (target - num) in num_set:
                return [num_set[target-num], num_index]
            num_set[num]=num_index