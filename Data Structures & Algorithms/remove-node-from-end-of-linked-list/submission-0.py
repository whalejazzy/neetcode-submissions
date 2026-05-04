# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        len = 0
        while temp is not None:
            temp = temp.next
            len += 1
        nb = len - n
        temp = head
        for i in range(nb - 1):
            temp = temp.next
        
        if nb == 0:
            return head.next
        if temp.next:
            temp.next = temp.next.next
        
        return head
        