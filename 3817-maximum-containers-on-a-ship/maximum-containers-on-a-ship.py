class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        deck = n * n
        if deck * w <= maxWeight:
            return deck
        else:
            return maxWeight // w