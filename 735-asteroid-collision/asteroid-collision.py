class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for i in asteroids:
            stack.append(i)

            while len(stack) >= 2:
                a = stack[-2]
                b = stack[-1]

                if a > 0 and b < 0:
                    if a < -b:
                        stack.pop(-2)
                    elif a == -b:
                        stack.pop()
                        stack.pop()
                    else:
                        stack.pop()
                else:
                    break
        return stack