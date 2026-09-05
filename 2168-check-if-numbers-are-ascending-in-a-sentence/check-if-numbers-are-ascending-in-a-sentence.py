class Solution(object):
    def areNumbersAscending(self, s):
        prev = 0
        for i in s.split():
            if i.isdigit():
                num = int(i)
                if num <= prev:
                    return False
                prev = num

        return True