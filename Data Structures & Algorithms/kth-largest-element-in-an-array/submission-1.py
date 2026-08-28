class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify(nums)

        while len(heap) > k:
            heapq.heappop(heap)
        
        return heap[0]