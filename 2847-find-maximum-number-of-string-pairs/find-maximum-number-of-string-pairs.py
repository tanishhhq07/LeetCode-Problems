class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        count = 0
        ans = set()

        for i in words:
            rev = i[::-1]

            if rev in ans:
                count += 1
            else:
                ans.add(i)

        return count
        