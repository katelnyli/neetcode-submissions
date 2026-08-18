class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        indegree = [[0] * n for _ in range(m)]


        for r in range(m):
            for c in range(n):
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    if (0 <= nr < m and 0 <= nc < n and matrix[nr][nc] < matrix[r][c]):
                        indegree[r][c] += 1
        
        q = deque()
        for r in range(m):
            for c in range(n):
                # if indegree 0, then its the smallest element adjacent to neighbors
                if indegree[r][c] == 0:
                    q.append([r, c])

        res = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    if (0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]):
                        indegree[nr][nc] -= 1
                        # once all smaller nodes have been visited, visit
                        if indegree[nr][nc] == 0:
                            q.append([nr, nc])
            res += 1
        
        return res

