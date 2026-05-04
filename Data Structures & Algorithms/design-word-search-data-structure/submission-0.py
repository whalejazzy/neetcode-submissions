class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            i = ord(w) - ord('a')
            if not node.children[i]:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.endOfWord = True
    
    def search(self, word: str) -> bool:
        def dfs(i, curr):
            for j in range(i, len(word)):
                if not curr:
                    return False
                c = word[j]
                if c == ".":
                    for child in curr.children:
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    child = curr.children[ord(c) - ord('a')]
                    if not child:
                        return False
                    curr = child
            return curr and curr.endOfWord
        return dfs(0, self.root)
