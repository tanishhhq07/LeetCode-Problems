class Solution(object):
    def pickGifts(self, gifts, k):
        for i in range(k):
            m = max(gifts)
            gifts[gifts.index(m)] = int(m ** 0.5)
        return sum(gifts)