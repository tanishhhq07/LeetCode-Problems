class Solution(object):
    def vowelConsonantScore(self, s):
        v = 0
        c = 0
        for i in s:
            if i.isalpha():
                if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                    v += 1
                else:
                    c += 1

        if c == 0:
            return 0
        return int(floor(v/c))
        