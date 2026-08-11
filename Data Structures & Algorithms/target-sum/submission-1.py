class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, summ):
            if i == len(nums):
                return 1 if summ == target else 0
            if (i, summ) in memo:
                return memo[(i, summ)]
            
            memo[(i, summ)] = (dfs(i + 1, summ - nums[i]) + dfs(i + 1, summ + nums[i]))
            return memo[(i, summ)]

        return dfs(0, 0)      
