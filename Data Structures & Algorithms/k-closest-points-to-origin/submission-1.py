class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for i in range(len(points)):
            x, y = points[i]
            dist = math.sqrt((x**2) + (y**2))
            heapq.heappush(heap, (dist, i))
        
        res = []
        for _ in range(k):
            idx = heapq.heappop(heap)[1]
            res.append(points[idx])
        
        return res
        

