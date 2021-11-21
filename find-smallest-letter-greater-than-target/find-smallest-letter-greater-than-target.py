class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[0] > target or letters[-1] <= target:
            return letters[0]
        left, right = 0, len(letters) - 1
        while left <= right:
            pivot = (left + right) // 2
            if letters[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1
        return letters[left]
        