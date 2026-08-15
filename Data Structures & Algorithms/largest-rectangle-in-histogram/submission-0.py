class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                bar = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                area = max(area, heights[bar] * (right - left - 1))
        
            stack.append(i)

        while stack:
            bar = stack.pop()
            left = stack[-1] if stack else -1
            right = len(heights)
            area = max(area, heights[bar] * (right - left - 1))

        return area


