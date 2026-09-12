class Solution(object):
    def interpret(self, command):
        arr = []
        for i in range(len(command)):
            if command[i] == "G":
                arr.append("G")
            if command[i] == "(" and command[i+1] == ")":
                arr.append("o")
            if command[i] == "(" and command[i+1] == "a" and command[i+2] == "l" and command[i+3] == ")":
                arr.append("al")
        return "".join(arr)