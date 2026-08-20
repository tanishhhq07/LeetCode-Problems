class Solution(object):
    def reverse(self, x):
        sign = 1
        if x < 0: 
            sign = -1
            x = -x

        n = 0
        while x != 0:
            a = x % 10
            n = n * 10 + a
            x = x // 10
            
        if n < -2147483648 or n > 2147483647:
            return 0

        return n * sign
