class Solution(object):
    def solveEquation(self, equation):
        lhs, rhs = equation.split("=")
        x1, x2 = 0, 0
        n1, n2 = 0, 0
        sign = 1
        num = 0
        flag = False
        for i in lhs:
            if i.isdigit():
                num = num * 10 + int(i)
                flag = True
            elif i == 'x':
                if flag:
                    x1 += sign * num
                else:
                    x1 += sign
                num = 0
                flag = False
            else:
                if flag:
                    n1 += sign * num
                if i == '+':
                    sign = 1
                else:
                    sign = -1
                num = 0
                flag = False

        if flag:
            n1 += sign * num

        sign = 1
        num = 0
        flag = False

        for i in rhs:
            if i.isdigit():
                num = num * 10 + int(i)
                flag = True
            elif i == 'x':
                if flag:
                    x2 += sign * num
                else:
                    x2 += sign
                num = 0
                flag = False
            else:
                if flag:
                    n2 += sign * num
                if i == '+':
                    sign = 1
                else:
                    sign = -1
                num = 0
                flag = False

        if flag:
            n2 += sign * num

        if x1 == x2:
            if n1 == n2:
                return "Infinite solutions"
            return "No solution"
        x = (n2 - n1) // (x1 - x2)

        return "x=" + str(x)

