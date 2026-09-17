class Solution(object):
    def findLongestWord(self, s, dictionary):
        ans = ""
        for a in dictionary:
            i = 0
            j = 0

            while i < len(s) and j < len(a):
                if s[i] == a[j]:
                    j += 1
                i += 1

            if j == len(a):
                if len(a) > len(ans):
                    ans = a
                elif len(a) == len(ans) and a < ans:
                    ans = a

        return ans
        