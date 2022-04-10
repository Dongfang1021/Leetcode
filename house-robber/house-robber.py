class Solution:
    def rob(self, nums: List[int]) -> int:
        yes = 0
        no = 0
        for i in nums:
            no, yes = max(no, yes), i + no
        return max(no, yes)
        