class Solution(object):
    def calculateTax(self, brackets, income):
        tax = 0
        prev = 0
        for upper, rate in brackets:
            if income > upper:
                tax += (upper - prev) * rate / 100.00
                prev = upper
            else:
                tax += (income - prev) * rate / 100.00
                break
        return tax