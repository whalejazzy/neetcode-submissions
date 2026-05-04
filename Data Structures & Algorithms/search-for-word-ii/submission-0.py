class Solution:
    class TrieNode:
        def __init__(self):
            self.children = [None]*26
            self.end = False
            self.reached = False
    class Trie:
        def __init__(self):
            self.root = Solution.TrieNode()
        def addWords(self, words):
            for word in words:
                curr = self.root
                for w in word:
                    if not curr.children[ord(w) - ord('a')]:
                        curr.children[ord(w) - ord('a')] = Solution.TrieNode()
                    curr = curr.children[ord(w) - ord('a')]
                curr.end = True
        
        def search(self, grid):
            m = len(grid)
            n = len(grid[0])
            
            dirs = [[1,0], [0, 1], [-1, 0], [0, -1]]
            
            def isValid(x, y, node):
                return x >= 0 and x < m and y >= 0 and  y < n and grid[x][y] != "#" and node.children[ord(grid[x][y]) - ord('a')]
            res = []
            path = []

            def dfs(node, x, y):
                if node.end and not node.reached:
                    node.reached = True
                    res.append(''.join(path))
                
                temp = grid[x][y]
                grid[x][y] = "#"
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if isValid(nx, ny, node):
                        c = grid[nx][ny]
                        path.append(c)
                        dfs(node.children[ord(c) - ord('a')], nx, ny)
                        path.pop()
                grid[x][y] = temp

            for x in range(m):
                    for y in range(n):
                        letter = grid[x][y]
                        if self.root.children[ord(letter) - ord('a')]:
                            path.append(letter)
                            dfs(self.root.children[ord(letter) - ord('a')], x, y)
                            path.pop()
            return res

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.Trie()	
        trie.addWords(words)
        return trie.search(board)