class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        distance = 0
        count = 0
        while mainTank > 0:
            mainTank -= 1
            distance += 10
            count += 1
            if count == 5 and additionalTank > 0:
                mainTank += 1
                additionalTank -= 1
                count = 0

        return distance