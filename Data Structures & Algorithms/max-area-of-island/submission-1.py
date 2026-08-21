class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            grid[i][j] = 0
            res = 1

            while q:
                r, c = q.popleft()

                for dx, dy in directions:
                    nr = r + dx
                    nc = c + dy

                    if nr < 0 or nr >= m or nc < 0 or nc >= n or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 0
                    res += 1

            return res
        
        area = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    area = max(area, bfs(r, c))

        return area

