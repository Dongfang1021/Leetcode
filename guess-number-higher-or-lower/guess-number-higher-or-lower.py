# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            pivot = (left + right) //2
            if guess(pivot) == -1:
                right = pivot - 1
            elif guess(pivot) == 1:
                left = pivot + 1
            else:
                return pivot