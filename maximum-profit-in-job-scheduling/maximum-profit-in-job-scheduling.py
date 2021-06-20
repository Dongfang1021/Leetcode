class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        start, end, pro = zip(*sorted(zip(startTime, endTime, profit), key=lambda x: x[0]))
        @lru_cache(None)
        def dp(i):
            if i == len(start):
                return 0
            j = bisect_left(start, end[i])
            return max(pro[i] + dp(j), dp(i + 1))
        return dp(0)