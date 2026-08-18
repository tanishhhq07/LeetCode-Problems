class Solution(object):
    def findWords(self, words):
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        f = []
        s = []
        t = []
        for i in words:
            if i[0].lower() in first:
                row = first
            elif i[0].lower() in second:
                row = second
            else:
                row = third
            check = True
            for ch in i:
                ch = ch.lower()
                if ch not in row:
                    check = False
                    break
            if check:
                if row == first:
                    f.append(i)
                elif row == second:
                    s.append(i)
                else:
                    t.append(i)
        return f + s + t