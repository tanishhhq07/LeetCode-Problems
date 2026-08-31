class Solution(object):
    def minOperations(self, grid, x):
        nums = []
        for row in grid:
            for i in row:
                nums.append(i)
        for i in nums:
            if i % x != nums[0] % x:
                return -1
        nums.sort()
        middle = nums[len(nums) // 2]
        count = 0
        for i in nums:
            count += abs(i - middle) // x

        return count