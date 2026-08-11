class Solution(object):
    def rob(self, nums):
        n = 0
        a = 0
        for i in nums:
            current = max(a, n + i)
            n = a
            a = current
        return a