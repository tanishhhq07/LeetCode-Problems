# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        while len(lists) > 1:
            newLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if i + 1 < len(lists):
                    list2 = lists[i + 1]
                else:
                    newLists.append(list1)
                    continue
                if not list1:
                    newLists.append(list2)
                    continue
                if not list2:
                    newLists.append(list1)
                    continue
                if list1.val < list2.val:
                    head = list1
                    list1 = list1.next
                else:
                    head = list2
                    list2 = list2.next

                curr = head
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

                newLists.append(head)
            lists = newLists

        return lists[0]
        