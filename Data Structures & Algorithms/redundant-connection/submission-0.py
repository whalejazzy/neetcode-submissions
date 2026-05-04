class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        neighbors = {node: [] for node in range(1 , len(edges) + 1)}
        
        def dfs(node, parent):
            if node in visited:
                return [parent, node]
            visited.add(node)
            for n in neighbors[node]:
                if n == parent:
                    continue
                res = dfs(n, node)
                if res is not None:
                    return res
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
            visited = set()
            if dfs(u, -1):
                return [u,v]
        