class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find_rotate_index(left,right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
        def bisearch(left, right):
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if nums[pivot] > target:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1
                    
        
        n = len (nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        rotate_index = find_rotate_index(0, n-1)
        if nums[rotate_index] == target:
            return rotate_index
        if rotate_index == 0:
            return bisearch(0, n-1)
        if target < nums[0]:
            return bisearch(rotate_index, n - 1)
        return bisearch(0, rotate_index)
    
        