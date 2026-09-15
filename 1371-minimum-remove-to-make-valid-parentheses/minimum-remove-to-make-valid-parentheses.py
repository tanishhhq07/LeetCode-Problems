class Solution(object):
    def minRemoveToMakeValid(self, s):
        ans = list(s)
        stk = []
        for i in range(len(ans)):
            if ans[i] == '(':
                stk.append(i)

            elif ans[i] == ')':
                if stk:
                    stk.pop()
                else:
                    ans[i] = ""

        while stk:
            i = stk.pop()
            ans[i] = ""

        return "".join(ans)
        