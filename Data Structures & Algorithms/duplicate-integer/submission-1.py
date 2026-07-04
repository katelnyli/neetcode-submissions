class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set();
        for n in nums:
            if n in dupes:
                return True
            dupes.add(n)
        return False
        
        