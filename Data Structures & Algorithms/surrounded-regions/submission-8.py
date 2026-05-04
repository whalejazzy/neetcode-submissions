class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = []
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(r, c):
            if (r in range(len(board))) and (c in range(len(board[r]))) and board[r][c] == "O" and (r, c) not in safe:
                safe.append((r,c))
                for dr, dc in directions:
                    dfs(r + dr, c + dc)
        
        
        for r in range(1, len(board) - 1):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][len(board[0]) - 1] == "O":
                dfs(r, len(board[0]) - 1)
        for c in range(1, len(board[0]) - 1):
            if board[0][c] == "O":
                dfs(0, c)
            if board[len(board) - 1][c] == "O":
                dfs(len(board) - 1, c)
        
        for r in range(1, len(board) - 1):
            for c in range(1, len(board[r]) - 1):
                if (r,c) not in safe:
                    board[r][c] = "X"

        