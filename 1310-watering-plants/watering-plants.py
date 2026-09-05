class Solution(object):
    def wateringPlants(self, plants, capacity):
        steps = 0
        k = capacity
        for i in range(len(plants)):
            if capacity < plants[i]:
                steps += 2 * i
                capacity = k

            capacity -= plants[i]
            steps += 1
        return steps