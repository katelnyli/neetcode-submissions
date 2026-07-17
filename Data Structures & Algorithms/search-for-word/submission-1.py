class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(idx, r, c):
            if idx == len(word):
                return True

            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx] or board[r][c] == '.':
                return False
            
            board[r][c] = "."
            res = dfs(idx + 1, r + 1, c) or dfs(idx + 1, r - 1, c) or dfs(idx + 1, r, c + 1) or dfs(idx + 1, r, c - 1)

            board[r][c] = word[idx]

            return res
            
        
        for r in range(m):
            for c in range(n):
                if dfs(0, r, c):
                    return True

        return False