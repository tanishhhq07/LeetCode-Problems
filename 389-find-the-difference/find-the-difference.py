class Solution(object):
    def findTheDifference(self, s, t):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in alphabet:
            if s.count(i) != t.count(i):
                return i
        