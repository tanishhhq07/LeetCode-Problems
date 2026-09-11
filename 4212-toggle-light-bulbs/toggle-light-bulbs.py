class Solution(object):
    def toggleLightBulbs(self, bulbs):
        on = [0] * 101
        ans = []

        for i in bulbs:
            if on[i] == 0:
                on[i] = 1
            else:
                on[i] = 0

        for i in range(1, 101):
            if on[i] == 1:
                ans.append(i)

        return ans