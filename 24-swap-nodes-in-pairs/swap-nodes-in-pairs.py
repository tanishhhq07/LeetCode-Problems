# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        head = fast
        prev = None

        while True:
            slow.next = fast.next
            fast.next = slow

            if prev:
                prev.next = fast

            prev = slow
            if not slow.next:
                break

            slow = slow.next
            if not slow.next:
                break

            fast = slow.next

        return head