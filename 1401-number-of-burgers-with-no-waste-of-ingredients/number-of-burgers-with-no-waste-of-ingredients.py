class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        arr = []
        if tomatoSlices % 2 != 0:
            return arr
        jumbo = (tomatoSlices - (2 * cheeseSlices)) // 2
        small = cheeseSlices - jumbo
        if jumbo < 0 or small < 0:
            return arr
        arr.append(jumbo)
        arr.append(small)
        return arr

