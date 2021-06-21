class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
        return low
        
        
        
        
        

        