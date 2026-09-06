class Solution(object):
    def commonChars(self, words):
        ch = "abcdefghijklmnopqrstuvwxyz"
        count = [100] * 26
        arr = []
        for i in words:
            temp = [0] * 26

            for j in i:
                temp[ch.index(j)] += 1

            for a in range(26):
                count[a] = min(count[a], temp[a])

        for i in range(26):
            for j in range(count[i]):
                arr.append(ch[i])

        return arr