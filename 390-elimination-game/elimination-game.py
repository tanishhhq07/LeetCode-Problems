class Solution(object):
    def lastRemaining(self, n):
        head = 1
        count = 1
        flag = True
        while n > 1:
            if flag or n % 2 == 1:
                head += count
            n = n // 2
            count *= 2
            flag = not flag
        return head
              
        
        
        