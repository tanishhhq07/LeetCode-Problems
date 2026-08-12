class Solution(object):
    def minOperations(self, nums, k):
        total = 0
        count = 0
        for i in nums:
            total += i
        while total % k != 0:
            if total == 0:
                break
            else:
                total -= 1
            count += 1
        return count
        
