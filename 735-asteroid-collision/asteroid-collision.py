class Solution(object):
    def asteroidCollision(self, asteroids):
        stk = []
        for i in asteroids:
            if not stk:
                stk.append(i)
            elif i>0:
                stk.append(i)
            elif i<0:
                if stk[-1]<0:
                    stk.append(i)
                else:
                    if stk[-1]==-i:
                        stk.pop()
                    elif stk[-1]>-i:
                        continue
                    else:
                        while stk and stk[-1]>0 and stk[-1]<-i:
                            stk.pop()
                        if not stk or stk[-1]<0:
                            stk.append(i)
                        elif stk[-1]==-i:
                            stk.pop()
                        else:
                            continue   
        return stk
