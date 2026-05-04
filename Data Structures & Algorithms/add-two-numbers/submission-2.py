# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dig = 1
        val1 = 0
        while l1:
            val1 += l1.val* dig
            dig*= 10
            l1 = l1.next
        dig = 1
        val2 = 0
        
        while l2:
            val2 += l2.val* dig
            dig*= 10
            l2 = l2.next
        val = val1 + val2
        if val == 0:
            return ListNode()
        head = curr = ListNode()
        while val:
            curr.next = ListNode(val%10)
            curr = curr.next
            val = val // 10
        return head.next


        
