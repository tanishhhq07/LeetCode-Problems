class Solution(object):
    def numberOfSpecialChars(self, word):
        count = 0
        ans = set(word)
        for i in ans:
            if i.islower() and i.upper() in ans:
                count += 1
        return count
        