class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        vals = set(nums)
        count = 1
        max_count = 1

        for n in vals:
            if n - 1 in vals:
                continue

            curr_val = n
            while curr_val + 1 in vals:
                count += 1
                curr_val += 1
                max_count = max(max_count, count)
            
            count = 1
        
        return max_count
                

            