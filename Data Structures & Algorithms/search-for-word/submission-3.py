class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = []
        path = []
        def backtrack(i, j, path, curr):
            if curr == word:
                res.append(True)
                return
            if len(curr) > len(word) or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            if board[i][j] == word[len(curr)]:
                curr += board[i][j]
                path.append((i,j))
                if (i + 1, j) not in path:
                    backtrack(i+1, j, path, curr)
                if (i, j + 1) not in path:
                    backtrack(i, j + 1, path, curr)
                if (i - 1, j) not in path:
                    backtrack(i - 1, j, path, curr)
                if (i, j - 1) not in path:
                    backtrack(i, j - 1, path, curr)
                path.pop()
                curr = curr[:-1]
        for i in range(len(board)):
            for j in range(len(board[i])):    
                backtrack(i, j, [], "")
        return any(res)