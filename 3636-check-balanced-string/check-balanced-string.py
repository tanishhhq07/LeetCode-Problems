class Solution(object):
    def isBalanced(self, num):
        odd,even = 0,0
        for i in range(0,len(num)):
            if i % 2 == 0:
                even += int(num[i])
            else:
                odd += int(num[i])
        return even == odd