class Solution(object):
    def averageValue(self, nums):
        count = 0
        total = 0
        for i in nums:
            if i % 3 == 0 and i % 2 == 0:
                total += i
                count += 1
        if count > 0:
            return total / count
        else:
            return 0