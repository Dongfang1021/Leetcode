class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p1 = 0
        p2 = 0
        total = 0
        res = float("inf")
        while (p2 < len(nums)):
            total = total + nums[p2]
            if total < target:
                p2 += 1
            else:
                res = min(res, p2 - p1 + 1)
                total = total - nums[p1] - nums[p2]
                p1 += 1
        return res if res<float("inf") else 0 
        
