class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] represents the number of ways to decode s[0..i] 
        if not s or s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            one_dig = int(s[i - 1])
            two_dig = int(s[i - 2 : i])

            # if single, inherit number of ways from prev digit
            if one_dig != 0:
                dp[i] += dp[i - 1]
            # if double, add number of ways from 2 digits before
            if 9 < two_dig < 27:
                dp[i] += dp[i - 2]

        return dp[n] 
            