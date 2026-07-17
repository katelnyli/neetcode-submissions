class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(l, r, s):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        res = []
        def dfs(start, path):
            # base case
            if start >= len(s):
                res.append(path[:])
                return

            for end in range(start, len(s)):
                if isPalindrome(start, end, s):
                    path.append(s[start : end + 1])
                    dfs(end + 1, path)
                    path.pop()
        
        dfs(0, [])
        return res