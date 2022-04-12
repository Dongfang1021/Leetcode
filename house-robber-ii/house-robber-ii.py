class Solution:
    def robRange(self, nums, start, end):
        yes, no = nums[start], 0
        for i in range(start+1, end):
            no, yes = max(no, yes), nums[i] + no
        return max(no, yes)
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.robRange(nums, 0, len(nums) - 1), self.robRange(nums,1,len(nums)))
    

        
        
        