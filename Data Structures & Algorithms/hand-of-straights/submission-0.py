class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        count = Counter(hand)
        sorted_keys = sorted(count.keys())

        for key in sorted_keys:
            if count[key] > 0:
                for i in range(1, groupSize):
                    # check if next consec number after has the same amt, if it doesn't then it can't exist
                    if count[key + i] < count[key]:
                        return False
                    count[key + i] -= count[key]

        return True
        


