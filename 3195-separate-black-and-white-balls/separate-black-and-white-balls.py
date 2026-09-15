class Solution(object):
    def minimumSteps(self, s):
        count = 0
        ans = 0
        for i in s:
            if i == "1":
                count += 1
            else:
                ans += count
        return ans