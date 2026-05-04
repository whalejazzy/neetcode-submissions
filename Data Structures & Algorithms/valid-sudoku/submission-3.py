class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[0]* 10 for _ in range(len(board[0]))]
        squares = [[0]* 10 for _ in range(len(board[0]))]
        for row in range(len(board)):
            rows = [0]*10
            for col in range(len(board[row])):
                cell = board[row][col]
                if cell != ".":
                    cell = int(board[row][col])
                    rows[cell] += 1
                    if rows[cell] > 1:
                        return False
                    cols[col][cell] += 1
                    if cols[col][cell] > 1:
                        return False
                    square = row//3 * 3 + col//3
                    squares[square][cell] += 1
                    if squares[square][cell] > 1:
                        return False
        return True