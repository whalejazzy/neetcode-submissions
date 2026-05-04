class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[i] != "#":
                i += 1
            length = int(s[j:i])
            i += 1
            j = i + length
            res.append(s[i:j])
            i = j
            print(i)
        return res