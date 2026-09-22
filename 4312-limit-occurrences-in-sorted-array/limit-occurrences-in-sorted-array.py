class Solution(object):
    def limitOccurrences(self, nums, k):
        ans = []
        count = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                count = 1
            else:
                count += 1
            if count <= k:
                ans.append(nums[i])

        return ans