class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        left = 0
        right = len(plants) - 1
        a = capacityA
        b = capacityB
        refil = 0
        while left < right:
            if a < plants[left]:
                refil += 1
                a = capacityA
            a -= plants[left]
            left += 1

            if b < plants[right]:
                refil += 1
                b = capacityB
            b -= plants[right]
            right -= 1
        if left == right and a < plants[left] and b < plants[left]:
            refil += 1
        return refil