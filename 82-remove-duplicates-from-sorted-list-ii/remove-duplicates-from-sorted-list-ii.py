# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        while head and head.next and head.val == head.next.val:
            value = head.val
            while head and head.val == value:
                head = head.next
            
        curr = head
        prev = None

        while curr and curr.next:
            if curr.val == curr.next.val:
                value = curr.val
                while curr and curr.val == value:
                    curr = curr.next
                prev.next = curr

            else:
                prev = curr
                curr = curr.next
        return head