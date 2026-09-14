class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        count = 0
        start = 0

        while count < n:
            curr = start
            prev = nums[curr]

            while True:
                next = (curr + k) % n
                temp = nums[next]
                nums[next] = prev
                prev = temp
                curr = next
                count += 1

                if curr == start:
                    break

            start += 1