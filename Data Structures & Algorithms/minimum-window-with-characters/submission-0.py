class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        if n < m:
            return ""

        chars = [0] * 128
        needed = m

        for c in t:
            chars[ord(c) - ord('A')] += 1

        i = 0
        min_len = float('inf')
        idx = 0
        for j in range(n):
            if chars[ord(s[j]) - ord('A')] > 0:
                needed -= 1
            chars[ord(s[j]) - ord('A')] -= 1

            while needed == 0:
                if (j - i + 1) < min_len:
                    min_len = j - i + 1
                    idx = i

                chars[ord(s[i]) - ord('A')] += 1
                if chars[ord(s[i]) - ord('A')] > 0:
                    needed += 1
                
                i += 1

        return s[idx : idx + min_len] if min_len != float('inf') else ""


