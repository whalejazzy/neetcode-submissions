class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        graph = [[0]*n for _ in range(m)]
        for i in range(m):
            graph[i][0] = 1
        for i in range(n):
            graph[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                graph[i][j] = graph[i - 1][j] + graph[i][j -1]
        return graph[m -1][n - 1]