class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitmp = {}
        l = 0
        out = 0
        for r in range(len(fruits)):
            fruitmp[fruits[r]] = fruitmp.get(fruits[r], 0) + 1
            while len(fruitmp.keys()) > 2:
                fruitmp[fruits[l]] -= 1
                if fruitmp[fruits[l]] == 0:
                    fruitmp.pop(fruits[l])
                l += 1
            out = max(out, r - l + 1)
        return out
            