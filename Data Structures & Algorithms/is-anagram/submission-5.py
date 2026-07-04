class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map1 = defaultdict(int)

        for letter in s:
            map1[letter] += 1
        
        for letter in t:
            if map1[letter] == 0:
                return False
            map1[letter] -= 1
        
        return True
        