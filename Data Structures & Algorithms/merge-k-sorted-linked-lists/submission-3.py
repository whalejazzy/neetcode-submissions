# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val    

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        q = [NodeWrapper(l) for l in lists]

        heapq.heapify(q)
        dummy = ListNode()
        tail = dummy
        while q:
            wrapper = heapq.heappop(q)
            tail.next = wrapper.node
            wrapper.node = wrapper.node.next
            tail = tail.next
            if wrapper.node:
                heapq.heappush(q, wrapper)
        return dummy.next



        