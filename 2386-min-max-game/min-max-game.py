class Solution(object):
    def minMaxGame(self, nums):
        arr = []
        while len(nums) > 1:
            for i in range(0, len(nums), 2):
                if (i // 2) % 2 == 0:
                    arr.append(min(nums[i], nums[i + 1]))
                else:
                    arr.append(max(nums[i], nums[i + 1]))
            nums = arr
            arr = []
        return nums[0]