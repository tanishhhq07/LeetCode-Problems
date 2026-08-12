class Solution(object):
    def triangularSum(self, nums):
        arr = []

        while len(nums) > 1:
            for i in range(len(nums) - 1):
                a = nums[i] + nums[i + 1]
                arr.append(a % 10)
            nums = arr
            arr = []
        return nums[0]