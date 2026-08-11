class Solution(object):
    def differenceOfSum(self, nums):
        elesum = 0
        digsum = 0
        for i in nums:
            elesum += i
            while i > 0:
                a = i % 10
                digsum += a
                i = i / 10
        return abs(elesum - digsum) 
