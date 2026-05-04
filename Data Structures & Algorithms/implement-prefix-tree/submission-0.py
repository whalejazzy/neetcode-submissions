class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.endOfWord = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            i = ord(w) - ord('a')
            
            if not node.children[i]:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            node = node.children[ord(w) - ord('a')]
            if not node:
                return False
        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            node = node.children[ord(w) - ord('a')]
            if not node:
                return False
        return True
        