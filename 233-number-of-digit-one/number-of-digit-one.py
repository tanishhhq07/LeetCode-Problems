class Solution(object):
    def countDigitOne(self, n):
        count = 0
        a = 1
        while a <= n:
            left = n // (a * 10)
            digit = (n // a) % 10
            right = n % a

            count += left * a
            if digit == 1:
                count += right + 1
            elif digit > 1:
                count += a
            a *= 10
        return count