class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = 0
        max_right = 0
        l = 0
        r = len(height) - 1
        total = 0

        while l < r:
            if height[l] > max_left:
                max_left = height[l]

            if height[r] > max_right:
                max_right = height[r]

            if max_left < max_right:
                total += max_left - height[l]
                l += 1
            else:
                total += max_right - height[r]
                r -= 1
        
        return total