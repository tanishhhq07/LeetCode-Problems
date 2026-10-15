class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        total = 0
        n = x
        while n > 0:
            total += n % 10
            n //= 10

        if x % total == 0:
            return total
        else:
            return -1