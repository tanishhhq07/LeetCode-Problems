class Solution(object):
    def isBalanced(self, num):
        odd,even = 0,0
        for i in range(0,len(num),2):
            even += int(num[i])
        for i in range(1,len(num),2):
            odd += int(num[i])
        return even == odd