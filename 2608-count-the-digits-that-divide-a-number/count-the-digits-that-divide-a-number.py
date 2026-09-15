class Solution(object):
    def countDigits(self, num):
        count = 0
        k = num
        while True:    
            a = k % 10
            if a == 0:
                break
            if num % a == 0:
                count += 1
            k /= 10
        return count