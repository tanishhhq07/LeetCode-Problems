class Solution(object):
    def calPoints(self, operations):
        arr = []
        score = 0
        for i in range(len(operations)):
            if operations[i].lstrip("-").isdigit():
                arr.append(int(operations[i]))
            elif operations[i] == "C":
                arr.pop()
            elif operations[i] == "D":
                arr.append(arr[-1] * 2)
            elif operations[i] == "+":
                arr.append(arr[-1] + arr[-2])
        for i in arr:
            score += i
        return score

        