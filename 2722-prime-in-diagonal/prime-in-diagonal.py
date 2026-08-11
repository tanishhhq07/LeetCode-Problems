class Solution(object):
    def diagonalPrime(self, nums):
        a = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if i == j or i + j == len(nums[0]) - 1:
                    a.append(nums[i][j])
        large = 0
        for n in a:
            if n < 2:
                continue
            prime = True
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    prime = False
                    break
            if prime and n > large:
                large = n
        return large