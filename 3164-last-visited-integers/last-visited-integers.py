class Solution(object):
    def lastVisitedIntegers(self, nums):
        seen = []
        ans = []
        k = 0
        for i in nums:
            if i > 0:
                seen.append(i)
                k = 0
            else:
                k += 1
                if k <= len(seen):
                    ans.append(seen[-k])
                else:
                    ans.append(-1)

        return ans