class Solution(object):
    def sortSentence(self, s):
        s = s.split()
        arr = []

        for i in range(1, len(s) + 1):
            for j in s:
                if j[-1] == str(i):
                    arr.append(j[:-1])

        return " ".join(arr) 