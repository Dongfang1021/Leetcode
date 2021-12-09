class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        d = OrderedDict()
        window = t + 1
        for i, n in enumerate(nums):
            while len(d) > k:
                d.popitem(last=False)
            if (b := n//window) in d:
                return True 
            if b - 1 in d and abs(d[b-1] - n) <= t:
                return True
            if b + 1 in d and abs(d[b+1] - n) <= t:
                return True
            d[b] = nums[i]  
        return False 