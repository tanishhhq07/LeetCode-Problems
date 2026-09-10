class Solution(object):
    def pickGifts(self, gifts, k):
        for i in range(k):
            a = 0
            for j in range(1, len(gifts)):
                if gifts[j] > gifts[a]:
                    a = j

            gifts[a] = int(gifts[a] ** 0.5)
        return sum(gifts)