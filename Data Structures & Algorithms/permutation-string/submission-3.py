class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        if n < 1 or m > n:
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26
        
        for i in range(m):
            freq1[ord(s1[i]) - ord("a")] += 1
            freq2[ord(s2[i]) - ord("a")] += 1

        if freq1 == freq2:
            return True
        
        for j in range(m, n):
            freq2[ord(s2[j]) - ord("a")] += 1
            freq2[ord(s2[j - m]) - ord("a")] -= 1
            if freq1 == freq2:
                return True

        return False
            
        
