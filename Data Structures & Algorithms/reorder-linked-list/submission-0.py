# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #slow is now the middle of the LL
        prev = None
        node = slow
        while node is not None:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        node = head

        while prev.next is not None:
            temp = node.next
            temp2 = prev.next
            node.next = prev
            prev.next = temp
            node = temp
            prev = temp2
        
