class Solution(object):
    def finalString(self, s):
        a = ""
        for i in s:
            if i == "i":
                temp = ""
                for j in range(len(a) - 1, -1, -1):
                    temp += a[j]
                a = temp
            else:
                a += i
        return a