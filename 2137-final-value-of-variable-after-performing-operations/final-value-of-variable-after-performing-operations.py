class Solution(object):
    def finalValueAfterOperations(self, operations):
        val = 0
        for i in operations:
            if i == "--X" or i == "X--":
                val -= 1
            elif i == "++X" or i == "X++":
                val += 1
        
        return val
        