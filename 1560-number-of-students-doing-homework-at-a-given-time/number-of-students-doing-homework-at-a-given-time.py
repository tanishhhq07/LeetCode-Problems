class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        count = 0
        for i,j in zip(startTime,endTime):
            if i <= queryTime <= j:
                count += 1
        return count