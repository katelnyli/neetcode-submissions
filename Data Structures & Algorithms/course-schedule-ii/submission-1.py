class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            prereq[pre].append(crs)
            indegree[crs] += 1

        q = deque()

        # courses with no remaining prereqs have indegree = 0
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            finish += 1

            for neighbor in prereq[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
            
        if finish != numCourses:
            return []
        
        return res

