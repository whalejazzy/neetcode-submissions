class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False

        neighbors = {node : [] for node in range(n)}
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        visited = set()
        def dfs(n, parent):
            if n in visited:
                return False
            visited.add(n)
            for node in neighbors[n]:
                if node == parent:
                    continue
                if not dfs(node, n):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
