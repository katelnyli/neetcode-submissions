class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 != 0:
            return False
        
        target = summ // 2

        dp = [False] * (target + 1)
        dp[0] = True

        # bounded knapsack
        for n in nums:
            for i in range(target, n - 1, -1):
                j = i - n
                dp[i] = dp[i] or dp[j]

        return dp[-1]