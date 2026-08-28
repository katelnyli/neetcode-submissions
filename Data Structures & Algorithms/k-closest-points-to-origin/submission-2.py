class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            x, y = p[0], p[1]

            dist = (x ** 2) + (y ** 2)

            heapq.heappush(heap, (-dist, p))

            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []

        for element in heap:
            res.append(element[1])
        
        return res
