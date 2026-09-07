class Solution(object):
    def distributeCandies(self, candyType):
        n = len(candyType)
        types = len(set(candyType))

        if types < n / 2:
            return types
        return n / 2