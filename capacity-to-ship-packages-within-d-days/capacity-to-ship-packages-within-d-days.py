class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def solve(limit, weights, d, n):
            i = 0
            s = 0
            count = 1
            while i < n:
                s += weights[i]
                if (s > limit):
                    count += 1
                    s = weights[i]
                i += 1
            if count <= d:
                return True
            else:
                return False
        left = 0
        right = sum(weights)
        mx = max(weights)
        n = len(weights)
        while (left <= right):
            mid = (left + right) // 2
            if mx <= mid and solve(mid, weights, days, n):
                right = mid - 1
            else:
                left = mid + 1
        return left