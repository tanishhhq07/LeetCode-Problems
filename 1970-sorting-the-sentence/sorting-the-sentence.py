class Solution(object):
    def sortSentence(self, s):
        arr = [""] * len(s.split())
        for i in s.split():
            num = int(i[-1])
            arr[num-1] = i[:-1]
        return " ".join(arr) 