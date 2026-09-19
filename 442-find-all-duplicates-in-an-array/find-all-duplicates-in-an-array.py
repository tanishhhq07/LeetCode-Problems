class Solution(object):
    def findDuplicates(self, nums):
        val = set()
        ans = []
        for i in nums:
            if i in val:
                ans.append(i)
            else:
                val.add(i)

        return ans
        