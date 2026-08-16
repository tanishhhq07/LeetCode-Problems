# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        left = head
        right = head
        
        while right and right.next:
            right = right.next.next
            left = left.next

        prev = None
        while left:
            temp = left.next
            left.next = prev
            prev = left
            left = temp
        
        a , b = head , prev
        while b:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        return True