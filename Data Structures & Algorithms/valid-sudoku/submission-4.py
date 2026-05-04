class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        col = [[0] *10 for _ in range(10)]
        square = [[0] *10 for _ in range(10)]
        for r in range(len(board)):
            row = [0] *10
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    coord = int(board[r][c])
                    row[coord] += 1
                    if row[coord] > 1:
                        return False
                    col[c][coord] += 1
                    if col[c][coord] > 1:
                        return False
                    idx =  (r//3)*3+c//3
                    square[idx][coord] += 1
                    if square[idx][coord] > 1:
                        return False
        return True
