# runtime beats 10.54%
# memory usage beats under 5%

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums, dp, i):
            l = len(nums)
            if i in [l-1, l-2]:
                return nums[i]
            if dp[i]:
                return dp[i]
            if None not in dp[i+2:]:
                return nums[i] + max(dp[i+2:])
            else:
                for j in range(i+1, l):
                    if not dp[j]:
                        dp[j] = helper(nums, dp, j)

                return nums[i] + max(dp[i+2:])
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        dp = [None for _ in range(len(nums))]
        dp[0] = helper(nums, dp, 0)
        dp[1] = helper(nums, dp, 1)
        return max(dp[0], dp[1])

