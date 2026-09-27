# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        first = list1
        for i in range(a - 1):
            first = first.next
        last = first

        for i in range(b - a + 2):
            last = last.next
        first.next = list2

        while list2.next:
            list2 = list2.next
        list2.next = last
        
        return list1
        