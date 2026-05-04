class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap = {num : set() for num in range(numCourses)}
        for post, pre in prerequisites:
            hmap[post].add(pre)
        print(hmap)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            visited.add(course)
            for post in hmap[course]:
                if not dfs(post):
                    return False
            visited.remove(course)
            return True
        return all([dfs(course) for course in hmap.keys()])