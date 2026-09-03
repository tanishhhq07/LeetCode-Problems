class Solution(object):
    def clearDigits(self, s):
        digits = "0123456789"
        arr = []
        for i in s:
            if i in digits:
                arr.pop()
            else:
                arr.append(i)

        return "".join(arr)
