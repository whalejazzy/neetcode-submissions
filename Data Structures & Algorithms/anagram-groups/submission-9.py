class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)
        for s in strs:
            alphabet = [0] * 26
            for c in s:
                alphabet[ord(c) - ord('a')]+= 1
            grp[tuple(alphabet)].append(s)
        return list(grp.values())