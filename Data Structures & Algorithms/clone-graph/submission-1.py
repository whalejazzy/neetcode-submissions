"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return 
        visited = {}
        def dfs(node):
            newNode = Node(node.val)
            visited[node] = newNode
            for n in node.neighbors:
                if n not in visited.keys():
                    dfs(n)
                newNode.neighbors.append(visited[n])
        
            return newNode
        return dfs(node)


