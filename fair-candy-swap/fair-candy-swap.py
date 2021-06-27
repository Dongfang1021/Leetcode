class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_alice, sum_bob = sum(aliceSizes), sum(bobSizes)
        set_bob = set(bobSizes)
        for i in aliceSizes:
            if i + (sum_bob - sum_alice)/ 2 in set_bob:
                return [i, i+(sum_bob - sum_alice)/2]
        