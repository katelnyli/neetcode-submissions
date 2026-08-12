class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        memo = {}

        def dfs(i, j):
            if i == m:
                return n - j
            
            if j == n:
                return m - i

            if (i, j) in memo:
                return memo[(i, j)]

            res = 0
            if word1[i] == word2[j]:
                res = dfs(i + 1, j + 1)
            else: 
                delete = dfs(i + 1, j)
                insert = dfs(i, j + 1)
                replace = dfs(i + 1, j + 1)
                res = min(delete, insert, replace) + 1
            
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)