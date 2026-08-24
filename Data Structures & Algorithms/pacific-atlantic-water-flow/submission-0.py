class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific = set()
        atlantic = set()

        def dfs(i, j, visited): 
            visited.add((i, j))

            for dx, dy in directions:
                nx, ny = i + dx, j + dy

                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in visited and heights[nx][ny] >= heights[i][j]:
                        dfs(nx, ny, visited)

        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n - 1, atlantic)

        for c in range(n):
            dfs(0, c, pacific)
            dfs(m - 1, c, atlantic)

        return list(pacific & atlantic)



            
            

