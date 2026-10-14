class Solution(object):
    def maximumScore(self, a, b, c):
        score = 0
        while (a > 0 and b > 0) or (b > 0 and c > 0) or (a > 0 and c > 0):
            if a >= b and a >= c:
                if b > 0:
                    a -= 1
                    b -= 1
                else:
                    a -= 1
                    c -= 1

            elif b >= a and b >= c:
                if a > 0:
                    b -= 1
                    a -= 1
                else:
                    b -= 1
                    c -= 1

            else:
                if a > 0:
                    c -= 1
                    a -= 1
                else:
                    c -= 1
                    b -= 1

            score += 1
        return score