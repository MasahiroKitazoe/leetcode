# https://leetcode.com/problems/symmetric-tree/ 
# runtime beats 76.5%
# memory usage beats 13.04%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def func(l, r):
            if not l and not r:
                return True
            elif l and r:
                if l.val != r.val:
                    return False
            else:
                return False
            
            is_outer_valid = func(l.left, r.right)
            is_inner_valid = func(l.right, r.left)
            return is_outer_valid and is_inner_valid
    
        if not root:
            return True
        return func(root.left, root.right)
