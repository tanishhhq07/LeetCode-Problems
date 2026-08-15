class Solution(object):
    def divisorSubstrings(self, num, k):
        count = 0
        n = num
        digit = 0
        while n > 0:
            digit += 1
            n //= 10
        tens = 1
        for i in range(k):
            tens *= 10
        n = num
        for i in range(digit - k + 1):
            x = n % tens
            if x != 0 and num % x == 0:
                count += 1
            n //= 10
        return count
        