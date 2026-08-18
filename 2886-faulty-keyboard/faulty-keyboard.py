class Solution(object):
    def finalString(self, s):
        a=[]
        i=0
        while i < len(s):
            if s[i]!='i':
                a.append(s[i])
            elif s[i]=='i':
                a.reverse()
            i+=1
        return "".join(a)