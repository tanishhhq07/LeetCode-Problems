class Solution(object):
    def getHint(self, secret, guess):
        bulls = 0
        cows = 0
        count = [0] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                a = int(secret[i])
                b = int(guess[i])
                if count[a] < 0:
                    cows += 1

                if count[b] > 0:
                    cows += 1

                count[a] += 1
                count[b] -= 1
        return str(bulls) + "A" + str(cows) + "B"