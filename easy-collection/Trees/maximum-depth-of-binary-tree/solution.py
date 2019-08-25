# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# runtime beats 78.83%
# memory usage beats 11.11%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def measure_depth(self, tree):
        rc = 0
        lc = 0
        if tree.right:
            rc += 1
            rc += self.measure_depth(tree.right)
        if tree.left:
            lc += 1
            lc += self.measure_depth(tree.left)
        return max(rc, lc)
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.measure_depth(root) + 1
            
