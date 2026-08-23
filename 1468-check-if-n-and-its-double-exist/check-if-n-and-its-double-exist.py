class Solution(object):
    def checkIfExist(self, arr):
        for a in arr:
            if a * 2 in arr:
                if a == 0 and arr.count(a) == 1:
                    continue
                return True
        return False