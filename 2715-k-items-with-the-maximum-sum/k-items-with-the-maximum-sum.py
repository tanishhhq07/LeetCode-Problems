class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        total = 0

        if k <= numOnes:
            return k

        total = numOnes
        k -= numOnes

        if k <= numZeros:
            return total

        k -= numZeros
        total -= k

        return total