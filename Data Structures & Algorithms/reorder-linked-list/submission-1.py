# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1, l2 = head, head
        while l2 and l2.next:
            l2 = l2.next.next
            l1 = l1.next
        
        curr = l1
        prev = None
        
        while l1 is not None:
            curr = l1
            l1 = l1.next
            curr.next = prev
            prev = curr

        while curr.next:
            temp1 = head.next
            temp2 = curr.next
            head.next = curr
            curr.next = temp1
            head = temp1
            curr = temp2
        
            