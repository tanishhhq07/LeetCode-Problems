class Solution(object):
    def minAddToMakeValid(self, s):
        stk = []
        for i in s:
            if not stk:
                stk.append(i)
            else:
                if i == '(':
                    stk.append('(')
                else:
                    if stk[-1] == '(':
                        stk.pop()
                    else:
                        stk.append(')')
        return len(stk)