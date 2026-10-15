class Solution(object):
    def getSneakyNumbers(self, nums):
        count = [0] * 100
        ans = []
        for num in nums:
            count[num] += 1

            if count[num] == 2:
                ans.append(num)

            if len(ans) == 2:
                return ans

        return ans




        