class Solution(object):
    def convertTemperature(self, celsius):
        K = celsius + 273.15
        F = celsius * 1.80 + 32.00
        return [K, F]