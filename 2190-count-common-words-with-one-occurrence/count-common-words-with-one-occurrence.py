class Solution(object):
    def countWords(self, words1, words2):
        count = 0
        for i in words1:
            c1 = 0
            c2 = 0
            for j in words1:
                if i == j:
                    c1 += 1
            for j in words2:
                if i == j:
                    c2 += 1
            if c1 == 1 and c2 == 1:
                count += 1
        return count