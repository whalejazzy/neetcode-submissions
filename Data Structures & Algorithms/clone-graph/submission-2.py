"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        mp = {}
        def dfs(n):
            if n in mp:
               currnode = mp[n]
               if currnode.neighbors != []:
                    return
            else:
                currnode = Node(n.val)
                mp[n] = currnode
            for child in n.neighbors:
                if child not in mp:
                    newnode = Node(child.val)
                    mp[child] = newnode
                currnode.neighbors.append(mp[child])
                dfs(child)
        dfs(node)
        return mp[node]
                


