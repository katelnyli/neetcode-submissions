class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        res = 0
        i = 0
        for j in range(len(s)):
            freqs[s[j]] += 1
            longest = max(freqs.values())

            while (j - i + 1) - longest > k:
                freqs[s[i]] -= 1
                i += 1
            
            res = max(res, j - i + 1)

        return res

            
