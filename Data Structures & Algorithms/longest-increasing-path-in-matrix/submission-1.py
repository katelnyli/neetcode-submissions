class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dp = {}

        def dfs(i, j, prevVal):
            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= prevVal:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = 1

            for dx, dy in directions:
                res = max(res, 1 + dfs(i + dx, j + dy, matrix[i][j]))
            
            dp[(i, j)] = res
            return res
        
        longest = 0

        for r in range(m):
            for c in range(n):
                longest = max(longest, dfs(r, c, float("-inf")))
        
        return longest
