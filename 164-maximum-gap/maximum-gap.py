class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        count = 0
        for i in range(len(nums) - 1):
            gap = nums[i + 1] - nums[i]
            if gap > count:
                count = gap
        return count
        