class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)
        n = len(s2)
        if n < l:
            return False

        chars1 = [0] * 26
        chars2 = [0] * 26

        for c in range(l):
            chars1[ord(s1[c]) - ord('a')] += 1
            chars2[ord(s2[c]) - ord('a')] += 1
        
        if chars1 == chars2:
                return True

        for i in range(l, n):
            chars2[ord(s2[i]) - ord('a')] += 1
            chars2[ord(s2[i - l]) - ord('a')] -= 1
            if chars1 == chars2:
                return True

        return False
            
            

