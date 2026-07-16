class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, remain, path):
            if remain == 0:
                res.append(path[:])
                return
            
            for i in range(idx, len(candidates)):
                if remain < candidates[i]:
                    break
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs(i + 1, remain - candidates[i], path)
                path.pop()

        dfs(0, target, [])
        return res