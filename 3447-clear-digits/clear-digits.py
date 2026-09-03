class Solution(object):
    def clearDigits(self, s):
        arr = []
        for i in s:
            if i.isdigit():
                arr.pop()
            else:
                arr.append(i)

        return "".join(arr)
