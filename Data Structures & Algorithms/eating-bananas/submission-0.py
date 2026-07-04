class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                return True
            
            return False


        n = len(piles) 
        i = 1
        j = max(piles)

        minTime = 0
        while i <= j:
            mid = (i + j) // 2

            if canFinish(mid):
                minTime = mid
                j = mid - 1
            else:
                i = mid + 1

        return minTime

