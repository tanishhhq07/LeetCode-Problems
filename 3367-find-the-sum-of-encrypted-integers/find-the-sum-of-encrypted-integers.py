class Solution(object):
    def sumOfEncryptedInt(self, nums):
        def encrypt(x):
            large = 0
            count = 0
            while x > 0:
                a = x % 10
                if a > large:
                    large = a
                count += 1
                x //= 10
            n = 0
            while count > 0:
                n = n * 10 + large
                count -= 1
            return n
        total = 0
        for i in nums:
            total += encrypt(i)
        return total