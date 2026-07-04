class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0; j = n - 1

        while i < j:
            mid = (i + j) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid

        pivot = j

        left = 0; right = n - 1
        while left <= right:
            mid = (left + right) // 2
            real_mid = (mid + pivot) % n

            if nums[real_mid] < target:
                left = mid + 1
            elif nums[real_mid] > target:
                right = mid - 1
            else:
                return real_mid

        return -1