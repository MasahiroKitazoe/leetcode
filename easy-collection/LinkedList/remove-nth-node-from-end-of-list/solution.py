# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# runtime beats 63.26%
# memory 13.9MB: beats under 5%

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            head = None
            return head

        node = head
        node.before = None
        while True:
            if not node.next:
                break
            node.next.before = node
            node = node.next
        for i in range(1, n):
            node = node.before
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
        else:
            node.before.next = None
        return head

