class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colcount = [[0]*10 for _ in range(len(board))]
        squarecount = [[0]*10 for _ in range(len(board))]
        for row in range(len(board)):
            rowcount = [0]*10
            for col in range(len(board)):
                if board[row][col] != ".":
                    num = int(board[row][col])
                    rowcount[num] += 1
                    if rowcount[num] > 1:
                        return False
                    
                    colcount[col][num] += 1
                    if colcount[col][num] > 1:
                        
                        return False
                    squarenum = (row//3)*3 + col//3
                    squarecount[squarenum][num] += 1
                    if squarecount[squarenum][num] > 1:
                        return False
        return True

