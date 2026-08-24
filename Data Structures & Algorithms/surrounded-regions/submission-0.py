class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or board[i][j] != "O":
                return 
            
            visited.add((i, j))

            for dx, dy in directions:
                dfs(i + dx, j + dy)

        for r in range(m):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][n - 1] == "O":
                dfs(r, n - 1)
        
        for c in range(n):
            if board[0][c] == "O":
                dfs(0, c)
            if board[m - 1][c] == "O":
                dfs(m - 1, c)

        for r in range(1, m):
            for c in range(1, n):
                if board[r][c] == "O" and (r, c) not in visited: 
                    board[r][c] = "X"
