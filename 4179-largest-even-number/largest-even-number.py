class Solution(object):
    def largestEven(self, s):
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "2":
                return s[:i + 1]

        return ""