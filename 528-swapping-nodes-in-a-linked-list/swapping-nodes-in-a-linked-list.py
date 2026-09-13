# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        slow = head
        fast = head
        for i in range(k-1):
            fast = fast.next
        knode = fast
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        knode.val , slow.val = slow.val , knode.val

        return head
        
        

        