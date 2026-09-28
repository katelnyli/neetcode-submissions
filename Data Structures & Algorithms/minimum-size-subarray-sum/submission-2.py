class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        i = 0
        curr_sum = 0
        for j in range(len(nums)):
            curr_sum += nums[j]

            while i <= j and curr_sum >= target:
                res = min(res, j - i + 1)
                curr_sum -= nums[i]
                i += 1

        return res if res != float("inf") else 0

