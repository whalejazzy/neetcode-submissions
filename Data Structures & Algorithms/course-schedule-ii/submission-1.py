class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for post, pre in prerequisites:
            prereq[post].append(pre)

        cycle = set()
        visit = set()
        output = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        for post in prereq.keys():
            if not dfs(post):
                return []
        return output
