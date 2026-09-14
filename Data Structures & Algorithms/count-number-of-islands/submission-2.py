class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or grid[i][j] == "0":
                return 
            
            visited.add((i, j))

            for x, y in directions:
                dfs(i + x, j + y)

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    res += 1
        
        return res

            
            
