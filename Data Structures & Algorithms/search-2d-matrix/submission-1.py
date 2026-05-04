class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(lst, l, r):
            if not lst:
                return False
            m = (r - l) // 2 +l
            if l > r:
                return False
            if lst[m] == target:
                return True
            elif lst[m] < target:
                return search(lst, m + 1, r)
            else: 
                return search(lst, l, m - 1)
        def listsearch(l, r):
            m = (r - l) // 2 + l
            if l > r:
                return []
            if matrix[m][0] <= target <= matrix[m][len(matrix[m]) -  1]:
                return matrix[m]
            elif matrix[m][len(matrix[m]) - 1] < target:
                return listsearch(m + 1, r)
            else: 
                return listsearch(l, m - 1)

        lst = listsearch(0, len(matrix) - 1)
        print(lst)
        return search(lst, 0, len(lst) - 1)
            
