# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        num1 = 0
        num2 = 0
        multiplier = 1
        while l1:
            num1 = num1 + l1.val*multiplier
            multiplier *=10
            l1 = l1.next
        multiplier = 1
        while l2:
            num2 = num2 + l2.val*multiplier
            multiplier *=10
            l2 = l2.next
        print(num1, num2)
        sum = num1 + num2
        l1 = head
        while sum:
            num = sum%10
            print(num)
            l1.val = num
            sum = sum // 10
            if sum and l1.next is None:
                l1.next = ListNode(0)
            l1 = l1.next
        return head