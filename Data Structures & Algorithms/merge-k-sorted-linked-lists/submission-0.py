# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = temp = ListNode()

        while any(lists):
            minVal, idx = 1001, -1
            for i in range(len(lists)):
                if lists[i] and lists[i].val < minVal:
                    minVal = lists[i].val
                    idx = i
            if idx != -1:
                temp.next = ListNode()
                temp = temp.next
                temp.val = minVal
                
                
                lists[idx] = lists[idx].next
        return res.next
            
