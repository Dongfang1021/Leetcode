class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = 0
        m = {}
        for num1 in nums1:
            for num2 in nums2:
                m[num1 + num2] = m.get(num1 + num2, 0) + 1
        for num3 in nums3:
            for num4 in nums4:
                cnt += m.get(-(num3 + num4), 0)
        return cnt
        