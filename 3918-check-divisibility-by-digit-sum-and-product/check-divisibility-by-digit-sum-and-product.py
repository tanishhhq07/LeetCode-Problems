class Solution(object):
    def checkDivisibility(self, n):
        if n < 10:
            return False
        total = 0
        product = 1
        temp = n
        while temp > 0:
            a = temp % 10
            temp //= 10
            total += a
            product *= a
        if n % (total + product) == 0:
            return True
        else:
            return False