class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        class Union:
            def __init__(self):
                self.par = {}
                self.size = {}
                self.components = 0
            def add(self, n):
                self.par[n] = n
                self.size[n] = 1
                self.components += 1
            def find(self, n):
                if self.par[n] != n:
                    self.par[n] = self.find(self.par[n])
                return self.par[n]
            def union(self, n1, n2):
                p1, p2 = self.find(n1), self.find(n2)
                if p1 == p2:
                    return False
                if self.size[p1] >= self.size[p2]:
                    self.par[p2] = p1
                    self.size[p1] += self.size[p2]
                else:
                    self.par[p1] = p2
                    self.size[p2] += self.size[p1]
                self.components -= 1
                return True
            def comp(self):
                return self.components

        dirs = [[-1, 0], [0, -1], [1, 0], [0,1]]
        res = []
        dsu = Union()
        for pos in positions:
            pos_tuple = tuple(pos)
            if pos_tuple not in dsu.par:
                dsu.add(pos_tuple)
                x, y = pos
                for dx, dy in dirs:
                    nei = (x+dx, y + dy)
                    if nei in dsu.par:
                        dsu.union(pos_tuple, nei)
            res.append(dsu.comp())
        return res