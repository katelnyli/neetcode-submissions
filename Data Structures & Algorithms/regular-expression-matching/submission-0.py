class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        dp = {}
        def dfs(i, j):
            if j == n:
                return i == m

            if (i, j) in dp:
                return dp[(i, j)]
            
            match = i < m and (s[i] == p[j] or p[j] == ".")

            if j + 1 < n and p[j + 1] == "*":
                # skip "char*" or include
                res = dfs(i, j + 2) or (match and dfs(i + 1, j))
            else:
                res = (match and dfs(i + 1, j + 1))
            
            dp[(i, j)] = res
            return res
        
        return dfs(0, 0)

            