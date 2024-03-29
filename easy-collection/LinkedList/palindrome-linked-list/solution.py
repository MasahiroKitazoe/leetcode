# https://leetcode.com/problems/palindrome-linked-list/
# runtime beats 59.73%
# memory usage beats under 5%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True

