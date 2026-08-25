class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses # number of prereqs for each course
        adj = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            indegree[pre] += 1
            adj[crs].append(pre)


        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        count = 0
        while q:
            node = q.popleft()
            count += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return count == numCourses