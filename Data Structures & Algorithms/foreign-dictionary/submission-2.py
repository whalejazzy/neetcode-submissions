class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {i : [] for word in words for i in word}
        n = len(words)
        for i in range(n - 1):
            word1 = words[i]
            word2 = words[i + 1]

            minlen = min(len(word1), len(word2))
            prefix = True
            for k in range(minlen):
                if word1[k] == word2[k]:
                    continue
                adj[word1[k]].append(word2[k])
                prefix = False
                break
            if prefix:
                if len(word1) > len(word2):
                    return ""

        visit = set()
        path = set()
        res = []
        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            visit.add(node)
            path.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            res.append(node)
            path.remove(node)
            return True
            
        for i in adj.keys():
            if not dfs(i):
                return ""
        res.reverse()
        return "".join(res)