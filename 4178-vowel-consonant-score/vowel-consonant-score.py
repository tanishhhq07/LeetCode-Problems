class Solution(object):
    def vowelConsonantScore(self, s):
        vowels = "aeiou"
        cons = "bcdfghjklmnpqrstvwxyz"
        v = 0
        c = 0
    
        for i in s:
            if i in cons:
                c += 1
            elif i in vowels:
                v += 1

        if c > 0:
            return int(floor(v/c))
        else:
            return 0
        