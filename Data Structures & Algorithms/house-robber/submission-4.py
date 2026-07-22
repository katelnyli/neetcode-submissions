class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] represents the maximum amount of money robbed at house i
        n = len(nums)
        if n == 1:
            return nums[0]

        prev = nums[0]
        curr = max(prev, nums[1])

        for i in range(2, n):
            temp = curr
            curr = max(nums[i] + prev, curr)
            prev = temp

        return curr