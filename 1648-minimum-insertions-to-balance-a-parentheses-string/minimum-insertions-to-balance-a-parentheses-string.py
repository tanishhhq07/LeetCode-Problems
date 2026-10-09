class Solution(object):
    def minInsertions(self, s):
        count = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                if count % 2 == 1:
                    ans += 1
                    count -= 1
                count += 2
            else:
                count -= 1
                if count < 0:
                    ans += 1
                    count = 1

        return ans + count