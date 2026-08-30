class Solution(object):
    def totalMoney(self, n):
        total = 0
        week = 1
        while n > 0:
            for i in range(7):
                if n == 0:
                    break
                total += week + i
                n -= 1
            week += 1
        return total