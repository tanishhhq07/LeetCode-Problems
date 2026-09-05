class Solution(object):
    def sortSentence(self, s):
        arr = [""] * len(s.split())
        num = 0
        for i in s.split():
            for j in i:
                if j.isdigit():
                    num = int(j)
                    arr[num -1] = i[:-1]
        return " ".join(arr) 