class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        fresh = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))

        time = 0
        while fresh > 0 and q:
            length = len(q)

            for _ in range(length):
                r, c = q.popleft()

                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1

                        

