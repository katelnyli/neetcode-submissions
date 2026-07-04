class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        time = self.store[key]
        if not time:
            return ""

        i = 0
        j = len(time) - 1
        res = ""

        while i <= j:
            mid = (i + j) // 2

            if time[mid][1] <= timestamp:
                res = time[mid][0]
                i = mid + 1 
            else:
                j = mid - 1
            
        return res
