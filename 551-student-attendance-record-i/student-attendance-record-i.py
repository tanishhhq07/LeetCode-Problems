class Solution(object):
    def checkRecord(self, s):
        a = 0
        l = 0
        for i in s:
            if i == "A":
                a += 1
                l = 0
                
            elif i == "L":
                l += 1

            else:
                l = 0
                
            if a >= 2 or l >= 3:
                return False
                
        return True