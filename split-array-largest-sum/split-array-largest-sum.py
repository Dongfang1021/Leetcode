class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid, sm, cnt = lo + (hi -lo) // 2, 0, 1
            for n in nums:
                sm, cnt = (n, cnt+1) if sm + n > mid else(sm + n, cnt)
            lo, hi = (mid + 1, hi) if cnt > m else (lo, mid)
        return lo