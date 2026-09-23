class Solution(object):
    def firstUniqChar(self, s):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        count = [0] * 26
        for i in s:
            count[alphabet.index(i)] += 1
        for i in range(len(s)):
            if count[alphabet.index(s[i])] == 1:
                return i

        return -1