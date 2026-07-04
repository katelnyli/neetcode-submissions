class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        max_len = 0
        i = 0

        for j in range(len(s)):
            while s[j] in chars:
                chars.remove(s[i])
                i += 1
            
            chars.add(s[j])

            max_len = max(max_len, j - i + 1)
            

        return max_len