"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = head
        newhead = newdummy = Node(0)
        
        nodes = {}
        while dummy is not None:
            newdummy = Node(dummy.val)
            nodes[dummy] = newdummy
            dummy = dummy.next
        dummy = head
        newdummy = newhead
        while dummy is not None:
            newdummy.next = nodes[dummy]
            newdummy_next = nodes.get(dummy.next, None)
            newdummy_random = nodes.get(dummy.random, None)
            newdummy.next.next = newdummy_next
            newdummy.next.random = newdummy_random

            dummy = dummy.next
            newdummy = newdummy.next
        return newhead.next
        