class Solution(object):
    def fractionAddition(self, expression):
        num1 = 0
        den1 = 1
        i = 0
        while i < len(expression):
            sign = 1
            if expression[i] == '-':
                sign = -1
                i += 1
            elif expression[i] == '+':
                i += 1
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            i += 1
            den = 0
            while i < len(expression) and expression[i].isdigit():
                den = den * 10 + int(expression[i])
                i += 1

            num1 = num1 * den + sign * num * den1
            den1 = den1 * den

        if num1 == 0:
            return "0/1"

        x = abs(num1)
        y = den1
        while y != 0:
            temp = x % y
            x = y
            y = temp
        return str(num1 // x) + "/" + str(den1 // x)