class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[i][j] represents how many ways to get to the curr sum j with i nums
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            for summ, ways in dp[i].items():
                dp[i + 1][summ + nums[i]] += ways
                dp[i + 1][summ - nums[i]] += ways
        
        return dp[n][target]


