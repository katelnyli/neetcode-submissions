class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        visited = set()

        def addCell(r, c):
            if min(r, c) < 0 or r == m or c == n or (r, c) in visited or grid[r][c] == -1:
                return 
            visited.add((r, c))
            q.append([r, c])
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        dist = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
