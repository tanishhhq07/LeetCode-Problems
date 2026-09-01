class Solution(object):
    def vowelConsonantScore(self, s):
        vowels = "aeiou"
        v = 0
        c = 0
        for i in s:
            if i.isalpha():
                if i in vowels:
                    v += 1
                else:
                    c += 1

        if c == 0:
            return 0
        return int(floor(v/c))
        