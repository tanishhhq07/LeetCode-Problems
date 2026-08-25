class Solution(object):
    def numSquares(self, n):
        count = [n + 1] * (n+1)
        count[0] = 0
        for i in range(1, n + 1):
            j = 1
            while (j * j) <= i :
                if count[i - (j * j)] + 1 < count[i]:
                    count[i] = count[i - (j * j)] + 1
                j += 1
        return count[n]
        