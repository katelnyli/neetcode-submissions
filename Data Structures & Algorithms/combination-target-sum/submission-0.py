class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, remain, path):
            if remain == 0:
                res.append(path[:])
                return

            for i in range(idx, len(nums)):
                if remain < nums[i]:
                    continue
                path.append(nums[i])
                dfs(i, remain - nums[i], path)
                path.pop()

        dfs(0, target, [])
        return res