class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        res = 0
        i = 0
        for j in range(len(s)):
            freqs[s[j]] += 1
            longest = max(freqs.values())
            length = j - i + 1
            while length - longest > k:
                freqs[s[i]] -= 1
                i += 1
                length -= 1
                longest = max(freqs.values())
            
            res = max(res, length)

        return res

            
