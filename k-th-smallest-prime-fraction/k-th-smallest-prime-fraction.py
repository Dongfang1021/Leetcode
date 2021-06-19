class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        from fractions import Fraction
        def under(x):
            count = best = 0
            i = -1
            for j in range(1, len(arr)):
                while arr[i + 1] < arr[j] * x:
                    i += 1
                count += i + 1
                if i >= 0:
                    best = max(best, Fraction(arr[i], arr[j]))
            return count, best
        low, high = 0.0, 1.0
        while high - low > 1e-9:
            mid = (low + high) / 2.0
            count, best = under(mid)
            if count < k:
                low = mid
            else:
                ans = best
                high = mid
        return ans.numerator, ans.denominator
        