# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1

        k = k % n

        if k == 0:
            return head

        curr.next = head
        curr = head

        for i in range(n - k - 1):
            curr = curr.next

        head = curr.next
        curr.next = None

        return head