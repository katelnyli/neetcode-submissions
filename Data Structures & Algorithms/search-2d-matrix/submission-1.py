class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix); n = len(matrix[0])
        i = 0; j = m * n - 1

        while i <= j:
            mid = (i + j) // 2
            r, c = divmod(mid, n)

            if r < m and matrix[r][c] < target:
                i = mid + 1
            elif c < n and matrix[r][c] > target:
                j = mid - 1
            else:
                return True
        
        return False