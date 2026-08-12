class Solution(object):
    def triangularSum(self, nums):
        n = len(nums)
        while n > 1:
            i = 0
            while i < n - 1:
                nums[i] = (nums[i] + nums[i + 1]) % 10
                i += 1
            n -= 1
        return nums[0]