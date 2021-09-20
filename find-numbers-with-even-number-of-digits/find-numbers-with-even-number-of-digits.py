class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return [len(str(num)) % 2 for num in nums].count(0)