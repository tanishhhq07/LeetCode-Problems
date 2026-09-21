class Solution(object):
    def freqAlphabets(self, s):
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9","10#", "11#", "12#", "13#", "14#", "15#", "16#","17#", "18#", "19#", "20#", "21#", "22#", "23#","24#", "25#", "26#"]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        ans = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                code = s[i:i + 3]
                i += 3
            else:
                code = s[i]
                i += 1
            ans += alphabet[numbers.index(code)]
        return ans