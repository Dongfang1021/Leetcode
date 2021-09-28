class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for index, value in enumerate(nums):
            if hashmap.get(value, -1) >= 0:
                diff = index - hashmap[value]
                if diff <= k:
                    return True
            hashmap[value] = index
        return False
            
        