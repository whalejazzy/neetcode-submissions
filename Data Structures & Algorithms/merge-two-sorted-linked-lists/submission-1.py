# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = retlist = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                retlist.next = list1
                list1 = list1.next
                retlist = retlist.next
            else:
                retlist.next = list2
                list2 = list2.next
                retlist = retlist.next
            
        while list2:
            retlist.next = list2
            list2 = list2.next
            retlist = retlist.next
        while list1:
            retlist.next = list1
            list1 = list1.next
            retlist = retlist.next
        return dummy.next
    