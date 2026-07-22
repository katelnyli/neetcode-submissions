class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l + 1 : r]

        max_len = 1
        res = s[0]
        for i in range(0, len(s) - 1):
            odd = expand(i, i)
            even = expand(i, i + 1)

            if len(odd) > max_len:
                max_len = len(odd)
                res = odd
            if len(even) > max_len:
                max_len = len(even)
                res = even
        
        return res

                