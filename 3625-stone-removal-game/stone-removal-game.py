class Solution(object):
    def canAliceWin(self, n):
        a = 10
        flag = True
        while n >= a:
            n -= a
            if n == 0:
                return flag
                
            a -= 1
            flag = not flag
        return not flag