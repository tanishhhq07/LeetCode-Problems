class Solution(object):
    def limitOccurrences(self, nums, k):
        ans = []
        for i in range(len(nums)):
            if i < k or nums[i] != nums[i - k]:
                ans.append(nums[i])
        return ans