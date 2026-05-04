class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = {node: [] for node in range(n)}
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u) 
        res = 0
        visited = set()
        def dfs(node, par):
            if node in visited:
                return
            visited.add(node)
            for v in neighbors[node]:
                if v == par:
                    continue
                else:
                    dfs(v, node)
        
        for node in neighbors.keys():
            if node in visited:
                continue
            dfs(node, -1)
            res += 1

        return res