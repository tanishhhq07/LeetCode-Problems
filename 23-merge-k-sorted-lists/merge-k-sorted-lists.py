# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None

        head = lists[0]
        for i in range(1, len(lists)):
            list1 = head
            list2 = lists[i]

            if not list1:
                head = list2
                continue

            if not list2:
                continue

            if list1.val < list2.val:
                newHead = list1
                list1 = list1.next
            else:
                newHead = list2
                list2 = list2.next

            curr = newHead
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next

                curr = curr.next

            if list1:
                curr.next = list1
            else:
                curr.next = list2

            head = newHead

        return head
        