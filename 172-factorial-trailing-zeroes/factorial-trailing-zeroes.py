class Solution(object):
    def trailingZeroes(self, n):
        count = 0
        a = 5
        while a <= n:
            count = count + n / a
            a *= 5
        return count

        