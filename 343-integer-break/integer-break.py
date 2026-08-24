class Solution(object):
    def integerBreak(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2
        total = 1
        while n > 4:
            total *= 3
            n -= 3
        total *= n
        return total