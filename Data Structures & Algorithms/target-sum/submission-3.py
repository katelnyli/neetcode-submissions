class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for summ, ways in dp.items():
                next_dp[summ + num] += ways
                next_dp[summ - num] += ways
            dp = next_dp

        return dp[target]