class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(first = 0):
            # if all integers are used up
            # if the first integer to consider has index n that means that the current permutation is done
            if first == len(nums):  
                output.append(nums[:])
            for i in range(first, len(nums)):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
                n = len(nums)
        output = []
        backtrack()
        return output