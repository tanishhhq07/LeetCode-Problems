class Solution(object):
    def pickGifts(self, gifts, k):
        for i in range (0, k):
            gifts = sorted(gifts)
            gifts[-1] = int((gifts[-1]) ** 0.5)
        return sum(gifts)