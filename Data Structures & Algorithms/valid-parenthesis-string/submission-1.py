class Solution:
    def checkValidString(self, s: str) -> bool:
        left = deque()
        stars = deque()

        for i in range(len(s)):
            if s[i] == "(":
                left.append(i)
            elif s[i] == "*":
                stars.append(i)
            else:
                if left:
                    left.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        
        while left and stars:
            if left.pop() > stars.pop():
                return False

        return not left