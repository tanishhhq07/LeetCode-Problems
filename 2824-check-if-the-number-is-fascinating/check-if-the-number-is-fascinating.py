class Solution(object):
    def isFascinating(self, n):
        digits = "123456789"
        a = str(n) + str(2 * n) + str(3 * n)
        if len(a) != 9 or '0' in a:
            return False
        for i in digits:
            if a.count(i) != 1:
                return False
        return True