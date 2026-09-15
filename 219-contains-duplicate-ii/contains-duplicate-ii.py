class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        arr = set()
        for i in range(len(nums)):
            if nums[i] in arr:
                return True
            arr.add(nums[i])
            if i >= k:
                arr.remove(nums[i - k])

        return False