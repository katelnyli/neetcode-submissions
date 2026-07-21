class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
            keep track of last idx of each char
            update max range of window based on last idx of already seen chars
            once reached, push the result, reset max range
        """

        lasts = {}
        
        for i in range(len(s)):
            lasts[s[i]] = i

        res = []
        max_range = 0
        i = j = 0
        for j in range(len(s)):
            max_range = max(max_range, lasts[s[j]])
            if j == max_range:
                res.append(j - i + 1)
                i = j + 1
                max_range = 0

        return res
