class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        boxes = {}
        for num in range(lowLimit, highLimit + 1):
            n = num
            total = 0
            while n > 0:
                total += n % 10
                n //= 10

            if total not in boxes:
                boxes[total] = 0

            boxes[total] += 1
        return max(boxes.values())
