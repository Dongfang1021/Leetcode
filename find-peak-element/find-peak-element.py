class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float("-inf"))
        nums.insert(0, float("-inf"))
        
        return self.helper(nums, 1, len(nums))
    
    def helper(self, nums, start, finish):
        if start > finish: return
        
        middle = start + (finish - start) // 2
        
        if nums[middle] > nums[middle - 1] and nums[middle] >  nums[middle + 1]:
            return middle - 1
        
        val = self.helper(nums, start, middle - 1)
        if val is None: val = self.helper(nums, middle + 1, finish)
        
        return val