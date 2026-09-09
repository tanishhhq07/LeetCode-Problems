class Solution(object):
    def countCommas(self, n):
        comma = 0
        a = 1000
        while a <= n:
            comma += (n - a + 1)
            a *= 1000
        return comma