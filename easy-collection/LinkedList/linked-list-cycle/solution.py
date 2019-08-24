# https://leetcode.com/problems/linked-list-cycle/
# runtime beats 81.01%
# memory usage beats under 5%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        nodes = {}
        while head:
            if head in nodes:
                return True
            nodes[head] = 1
            head = head.next
        return False
