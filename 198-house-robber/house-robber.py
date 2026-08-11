class Solution(object):
    def rob(self, nums):
        n = 0
        a = 0
        for i in nums:
            total = max(a, n + i)
            n = a
            a = total
        return a