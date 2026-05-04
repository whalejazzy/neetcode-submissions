class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        currFruit = {}
        l = 0
        r = 0
        out = 1
        while r < len(fruits):
            currFruit[fruits[r]] = currFruit.get(fruits[r], 0) + 1
            

            while len(currFruit.keys()) > 2:
                currFruit[fruits[l]] -= 1
                if currFruit[fruits[l]] == 0:
                    currFruit.pop(fruits[l], None)
                l += 1
            out = max(out, r - l + 1)
            r += 1
        return out

