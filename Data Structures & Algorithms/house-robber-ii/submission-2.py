class Solution:
    def rob(self, nums: List[int]) -> int:
        def max_rob(nums):
            if len(nums) == 1:
                return nums[0]
            
            prev = nums[0]
            curr = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                temp = curr
                curr = max(nums[i] + prev, curr)
                prev = temp
            
            return curr
        
        if len(nums) == 1:
            return nums[0]
        return max(max_rob(nums[:-1]), max_rob(nums[1:]))