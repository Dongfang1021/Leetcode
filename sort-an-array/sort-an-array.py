class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(A, low, high):
            if low >= high: return 
            p = partition(A, low, high) 
            quicksort(A, low, p-1) 
            quicksort(A, p+1, high)
        
        def partition(A, low, high):
            mid = (low + high)//2
            A[high], A[mid] = A[mid], A[high]
            i = low - 1
            for j in range(low, high):
                if A[j] < A[high]:
                    i = i + 1
                    A[i], A[j] = A[j], A[i]
            A[high], A[i+1] = A[i+1], A[high]
            return i + 1
        quicksort(nums, 0, len(nums) - 1)
        return nums
