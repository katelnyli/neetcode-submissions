class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] is T if s[:i] is in word dict or a valid word segment
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                j = i - len(word)
                if j >= 0 and dp[j] and s[j:i] == word:
                    dp[i] = True
                    break

        return dp[n]

