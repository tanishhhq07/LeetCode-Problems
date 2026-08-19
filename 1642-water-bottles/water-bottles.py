class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total = numBottles
        while numBottles >= numExchange:
            a = numBottles // numExchange
            b = numBottles % numExchange
            total += a
            numBottles = a + b
        return total
        