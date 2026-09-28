class Solution(object):
    def maxDepth(self, s):
        count = 0
        total = 0
        for i in s:
            if i == '(':
                count += 1
                if count > total:
                    total = count
            elif i == ')':
                count -= 1
        return total