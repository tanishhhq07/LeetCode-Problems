class Solution(object):
    def hasGroupsSizeX(self, deck):
        count = {}
        for i in deck:
            count[i] = count.get(i, 0) + 1
        for x in range(2, len(deck) + 1):
            possible = True
            for value in count.values():
                if value % x != 0:
                    possible = False
                    break
            if possible:
                return True
        return False