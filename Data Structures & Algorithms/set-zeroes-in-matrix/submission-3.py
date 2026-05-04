class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero = set()
        row = set()
        col = set()

        def clearcol(j):
            for x in range(len(matrix)):
                matrix[x][j] = 0
        
        def clearrow(i):
            for x in range(len(matrix[i])):
                matrix[i][x] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero.add((i, j))
        for i, j in zero:
            clearcol(j)
            clearrow(i)

        
                    
                    


                

        
        

        

        
        