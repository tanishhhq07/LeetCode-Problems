class Solution(object):
    def minOperations(self, nums, k):
        total = 0
        for i in nums:
            total += i
        a = total % k
        return a
        
