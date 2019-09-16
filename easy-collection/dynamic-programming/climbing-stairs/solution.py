# runtime beats 68.8%
# memory usage beats under 5%
# https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(n, memo):
            if n == 0:
                return 1
            elif n == 1:
                return 1
            if memo[n] == 0:
                memo[n] = helper(n-1, memo) + helper(n-2, memo)
            return memo[n]
        memo = [0 for _ in range(n+1)]
        return helper(n, memo)
