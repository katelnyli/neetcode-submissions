class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        last = [nums[0]]

        for i in range(1, len(nums)):
            if last[-1] < nums[i]:
                last.append(nums[i])
                continue
            
            l = 0
            r = len(last)

            while l < r:
                mid = (l + r) // 2

                if last[mid] < nums[i]:
                    l = mid + 1
                else:
                    r = mid
            
            last[l] = nums[i]
        
        return len(last)
