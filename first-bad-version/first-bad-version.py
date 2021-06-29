# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            pivot = left + (right - left ) //2
            if isBadVersion(pivot):
                right = pivot
            else:
                left = pivot + 1
        return left
        