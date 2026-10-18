class Solution(object):
    def isAnagram(self, s, t):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        if len(s) != len(t):
            return False

        for ch in alphabet:
            count1 = 0
            count2 = 0

            for c in s:
                if c == ch:
                    count1 += 1

            for c in t:
                if c == ch:
                    count2 += 1

            if count1 != count2:
                return False

        return True