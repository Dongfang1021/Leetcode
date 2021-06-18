class Solution:
    
    
    
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def enough(x):
            count = 0
            for i in range(1, m+1):
                count += min(x // i, n)
            return count >= k
        
        low,high = 1, m*n
        while low < high:
            mid = (low + high) / 2
            if not enough(mid):
                low = mid + 1
            else:
                high = mid
        return int(low)
        
        