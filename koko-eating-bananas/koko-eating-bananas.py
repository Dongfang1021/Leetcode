class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(k):
            H = 0
            for pile in piles:
                H += ((pile - 1)//k) + 1
            return H <= h
        best = max(piles)
        left, right, mid = 1, best, 0
        while left <= right:
            mid = (left + right) // 2
            if can_eat(mid):
                right = mid - 1
                best = mid
            else:
                left = mid + 1
        return best