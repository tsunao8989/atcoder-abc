class Solution:
    def isPalindrome(self, x: int) -> bool:
        y, s = x, 0
        while y > 0:
            s *= 10
            s += y % 10
            y //= 10
        f = True if int(x) == int(s) and int(x) >= 0 else False
        return f
