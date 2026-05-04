class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i : [] for i in range(numCourses)}
        for post, pre in prerequisites:
            courses[post].append(pre)
        visited = set()
        cycle = set()
        out = []
        def dfs(x):
            if x in cycle:
                return False
            if x in visited:
                return True
            visited.add(x)
            cycle.add(x)
            for c in courses[x]:
                if not dfs(c):
                    return False
            out.append(x)
            cycle.remove(x)
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return out