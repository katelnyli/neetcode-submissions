class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []
        
        if not digits:
            return res
            
        def dfs(idx, path):
            if idx == len(digits):
                res.append("".join(path))
                return
            
            for i in range(len(letters[digits[idx]])):
                path.append(letters[digits[idx]][i])
                dfs(idx + 1, path)
                path.pop()

        dfs(0, [])
        return res