class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idx, path):
            if idx == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[idx])
            dfs(idx + 1, path)

            path.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            dfs(idx + 1, path)
    
        dfs(0, [])
        return res