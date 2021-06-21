class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]: # nums[pivot] is the largest number in nums
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]: # nums[pivot] after rotate index
                        right = pivot - 1
                    else: # nums[pivot] before rotate index
                        left = pivot + 1
        
        def search(left, right): # binary search function
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1
        
        n = len(nums)
        if n == 1: # array just has one integer
            return 0 if nums[0] == target else -1
        rotate_index = find_rotate_index(0, n-1)
        if nums[rotate_index] == target:
            return rotate_index
        if rotate_index == 0:
            return search(0, n-1)
        if target < nums[0]:
            return search(rotate_index, n - 1)
        return search(0, rotate_index)
    
        