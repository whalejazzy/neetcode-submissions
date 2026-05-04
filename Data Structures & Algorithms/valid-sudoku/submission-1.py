class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colcount = [{} for _ in range(len(board))]
        squarecount = [{} for _ in range(len(board))]
        n = 0
        for i, row in enumerate(board):
            rowcount = {}
            print(n)
            n += 1
            for j, num in enumerate(row):
                if num != ".":
                    rowcount[num] = rowcount.get(num, 0) + 1
                    if rowcount[num] > 1:
                        return False

                    colcount[j][num] = colcount[j].get(num, 0) + 1
                    if colcount[j][num] > 1:
                        return False
                    
                    squarenum = ((i//3)*3 + j//3)
                    print(num, squarenum)
                    squarecount[squarenum][num] = squarecount[squarenum].get(num, 0) + 1
                    
                    if squarecount[squarenum][num] > 1:
                        return False
        return True


