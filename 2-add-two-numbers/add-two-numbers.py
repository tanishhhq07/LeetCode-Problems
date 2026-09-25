# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = None
        curr = None
        carry = 0
        while l1 or l2 or carry:
            a = 0
            b = 0

            if l1:
                a = l1.val
                l1 = l1.next

            if l2:
                b = l2.val
                l2 = l2.next

            total = a + b + carry
            carry = total // 10
            node = ListNode(total % 10)

            if head is None:
                head = node
                curr = node
            else:
                curr.next = node
                curr = node

        return head