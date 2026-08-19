class Solution(object):
    def maxBottlesDrunk(self, numBottles, numExchange):
        total = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange
            numBottles += 1
            total += 1
            numExchange += 1
        return total
        