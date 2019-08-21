# https://leetcode.com/problems/reverse-linked-list/
# runtime beats 95.66%
# memory usage beats 31.82%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        slow.next = None
        while True:
            n = fast.next
            fast.next = slow
            slow = fast
            if n:
                fast = n
            else:
                break
        return fast
