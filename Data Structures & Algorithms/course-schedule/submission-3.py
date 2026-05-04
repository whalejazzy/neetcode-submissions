class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {c: [] for c in range(numCourses)}
        for post, pre in prerequisites:
            courses[post].append(pre)
        visit = set()
        #completed = set()

        def dfs(c):

            if c in visit:
                return False
            # if c in completed:
            #     return True
            visit.add(c)
            for pre in courses[c]:
                if not dfs(pre):
                    return False
            
            visit.remove(c)
            
            #completed.add(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
