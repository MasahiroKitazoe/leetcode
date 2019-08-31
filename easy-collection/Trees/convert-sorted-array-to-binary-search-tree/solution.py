# Definition for a binary tree node.
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# runtime beats 85.81%
# memory usage beats 40.91%

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        def helper(nums):
            i = len(nums) // 2
            tree = TreeNode(nums[i])
            tree.left = helper(nums[:i]) if nums[:i] else None
            tree.right = helper(nums[i+1:]) if nums[i+1:] else None
            return tree
        
        return helper(nums)
