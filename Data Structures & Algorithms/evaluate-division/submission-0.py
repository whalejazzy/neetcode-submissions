class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, (a, b) in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        def dfs(curr, end, tot, visit):
            if curr == end:
                return tot
            visit.add(curr)
            for nxt, val in adj[curr]:
                if nxt not in visit:
                    res = dfs(nxt, end, tot * val, visit)
                    if res != -1:
                        return res
            return -1.0

        results = []
        for a, b in queries:
            if a not in adj or b not in adj:
                results.append(-1.0)
            else:
                results.append(dfs(a, b, 1.0, set()))
        return results