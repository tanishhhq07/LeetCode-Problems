class Solution(object):
    def numberOfMatches(self, n):
        match = 0
        while n >= 2:
            if n % 2 == 0:
                match += (n / 2)
                n = n / 2
            else:
                match += (n // 2) + 1
                n = (n // 2)
        return match