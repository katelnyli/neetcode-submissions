class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        max_len = 0
        freqs = defaultdict(int)
        
        i = 0
        for j in range(len(s)):
            freqs[s[j]] += 1
            max_freq = max(freqs.values())

            while (j - i + 1) - max_freq > k:
                freqs[s[i]] -= 1
                i += 1
            
            max_len = max(max_len, j - i + 1)

        return max_len