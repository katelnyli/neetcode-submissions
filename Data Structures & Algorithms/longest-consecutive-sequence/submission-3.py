class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        max_count = 0

        for n in vals:
            if n - 1 in vals:
                continue
            
            count = 1
            curr_val = n
            while curr_val + 1 in vals:
                count += 1
                curr_val += 1
            
            max_count = max(max_count, count)
        
        return max_count
                

            