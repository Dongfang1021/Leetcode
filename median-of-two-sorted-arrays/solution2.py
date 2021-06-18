class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = []
        for i in nums1:
            total.append(i)
        for i in nums2:
            total.append(i)
        total = sorted(total)
        if len(total) % 2 == 0:
            x = len(total) - 2
            z = x // 2
            ans = (total[z] + total[z+1]) / 2
            return ans
        elif len(total) % 2 != 0:
            x = len(total) - 1
            z = x // 2
            ans = total[z]
            return ans
