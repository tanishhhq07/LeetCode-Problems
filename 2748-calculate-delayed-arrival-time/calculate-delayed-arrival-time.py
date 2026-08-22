class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        total = (arrivalTime + delayedTime) % 24
        if total >= 24:
            return 0
        else:
            return total
        