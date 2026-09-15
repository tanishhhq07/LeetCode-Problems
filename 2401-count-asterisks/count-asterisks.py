class Solution(object):
    def countAsterisks(self, s):
        count = 0
        bars = 0

        for i in s:
            if i == "|":
                bars += 1
            elif i == "*" and bars % 2 == 0:
                count += 1

        return count