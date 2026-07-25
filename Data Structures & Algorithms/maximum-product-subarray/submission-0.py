class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minn = 1
        maxx = 1
        res = nums[0]

        for num in nums:
            curr_max = maxx * num
            curr_min = minn * num
            minn = min(curr_min, curr_max, num)
            maxx = max(curr_max, curr_min, num)
            res = max(res, maxx)

        return res