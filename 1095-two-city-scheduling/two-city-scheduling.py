class Solution(object):
    def twoCitySchedCost(self, costs):
        n = len(costs) // 2
        total = 0
        arr = []

        for i in costs:
            total += i[0]
            arr.append(i[1] - i[0])

        arr.sort()
        for i in range(n):
            total += arr[i]

        return total