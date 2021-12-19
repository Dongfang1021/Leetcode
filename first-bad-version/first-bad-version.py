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
        left, right = 0, n - 1
        while left <= right:
            pivot = (left + right) // 2
            if isBadVersion(pivot):
                right = pivot - 1
            else:
                left = pivot + 1
        return left 

        