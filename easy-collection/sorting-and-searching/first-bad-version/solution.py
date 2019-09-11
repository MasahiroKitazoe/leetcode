# https://leetcode.com/problems/first-bad-version/
# runtime beats 99.87%
# memory usage beats 52.78%

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
             return 1
        i = 0
        while True:
            t = (i + n) // 2
            is_i_bad = isBadVersion(t)
            is_before_bad = isBadVersion(t - 1)
            if is_i_bad and not is_before_bad:
                return t
            if is_i_bad:
                n = t - 1
            else:
                i = t + 1

