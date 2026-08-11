class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        n = 0
        a = 0
        for i in nums[1:]:
            total = max(a, n + i)
            n = a
            a = total
        first = a
        n = 0
        a = 0
        for i in nums[:-1]:
            total = max(a, n + i)
            n = a
            a = total
        second = a
        return max(first, second)
        