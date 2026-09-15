class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dup = {}
        for i in range(len(nums)):
            if nums[i] in dup and i - dup[nums[i]] <= k:
                return True
            
            dup[nums[i]] = i

        return False