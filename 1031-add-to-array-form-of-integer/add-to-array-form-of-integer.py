class Solution(object):
    def addToArrayForm(self, num, k):
        total = 0
        ans = []
        for digit in num:
            total = total * 10 + digit
        
        total += k
        while total > 0:
            ans.append(total % 10)
            total //= 10

        ans.reverse()
        return ans
        