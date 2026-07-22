class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def expand(l, r):
            count = 0
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            
            return count
        
        summ = 0
        for i in range(n):
            odd = expand(i, i)
            even = expand(i , i + 1) 
            summ += odd + even

        return summ
