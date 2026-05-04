class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        board = [["."] * n for a in range(n)]
        def validQueen(x, y, board):
            i = x - 1
            j = y - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            i = x - 1
            j = y + 1
            while i >= 0 and j < len(board):
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            for a in range(x, -1, -1):
                if board[a][y] == "Q":
                    return False
            for a in range(y, -1, -1):
                if board[x][a] == "Q":
                    return False
            return True
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if validQueen(r, c, board):
                    board[r][c] ="Q"
                    backtrack(r+1)
                    board[r][c] = "."
        backtrack(0)
        return res


            
            

                

                    
            