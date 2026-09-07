class Solution(object):
    def distributeCandies(self, candyType):
        n = len(candyType)
        types = len(set(candyType))

        return min(types , n // 2)