class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = (r - l)// 2 + l
            print(m)
            if matrix[m][0] <= target and matrix[m][len(matrix[0]) - 1] >= target: # found row
                a = 0
                b = len(matrix[0]) - 1
                while a <= b:
                    c = (b - a) //2 + a
                    if matrix[m][c] == target:
                        return True
                    elif matrix[m][c] < target:
                        a = c + 1
                    else:
                        b = c - 1
                return False
            elif matrix[m][0] > target:
                r = m - 1
            elif matrix[m][len(matrix[0]) - 1] < target:
                l = m + 1
        return False  