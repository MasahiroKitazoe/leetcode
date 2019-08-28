# https://leetcode.com/problems/binary-tree-level-order-traversal/
# runtime beats 78.98%
# memory usage beats 82.35%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def helper(nodes):
            r = []
            for node in nodes:
                if node:
                    r.append(node.left)
                    r.append(node.right)
            return r
        
        ll = []
        nodes = [root]
        while any(nodes):
            ll.append(nodes)
            nodes = helper(nodes)
        return [[node.val for node in l if node]for l in ll]
        
