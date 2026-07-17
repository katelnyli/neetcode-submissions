class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openn, close, path):
            if openn == close == n:
                res.append("".join(path))
                return
            
            if openn < n:
                path.append("(")
                dfs(openn + 1, close, path)
                path.pop()
            if close < openn:
                path.append(")")
                dfs(openn, close + 1, path)
                path.pop()

        dfs(0, 0, [])
        return res