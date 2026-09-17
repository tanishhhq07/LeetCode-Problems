class Solution(object):
    def findLongestWord(self, s, dictionary):
        ans = ""

        for a in dictionary:
            i = 0
            for k in s:
                if i < len(a) and k == a[i]:
                    i += 1

            if i == len(a):
                if len(a) > len(ans):
                    ans = a
                elif len(a) == len(ans) and a < ans:
                    ans = a

        return ans
        