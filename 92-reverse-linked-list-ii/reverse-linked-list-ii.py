# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if left == right:
            return head
        curr = head
        prev = None

        for i in range(left - 1):
            prev = curr
            curr = curr.next

        first = prev
        start = curr
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        if first:
            first.next = prev
        else:
            head = prev
        start.next = curr
        return head