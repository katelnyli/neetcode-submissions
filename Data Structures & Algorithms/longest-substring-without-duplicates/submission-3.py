class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)
        i = 0
        seen = set()
        for j in range(n):
            while s[j] in seen:
                seen.discard(s[i])
                i += 1
            
            seen.add(s[j])

            res = max(res, j - i + 1)

        return res



            
