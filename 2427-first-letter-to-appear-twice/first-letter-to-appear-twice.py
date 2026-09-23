class Solution(object):
    def repeatedCharacter(self, s):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        seen = [0] * 26
        for i in s:
            index = alphabet.index(i)
            if seen[index] == 1:
                return i
            seen[index] = 1

        return ""
        