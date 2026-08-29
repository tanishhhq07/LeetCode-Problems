class Solution(object):
    def arraySign(self, nums):
        total = 1
        for i in nums:
            total *= i
        if total < 0:
            return -1
        elif total > 0:
            return 1
        else:
            return 0