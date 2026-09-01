class Solution(object):
    def isWinner(self, player1, player2):
        score1 = 0
        score2 = 0

        for i in range(len(player1)):
            if i > 0 and player1[i-1] == 10:
                score1 += player1[i] * 2
            elif i > 1 and player1[i-2] == 10:
                score1 += player1[i] * 2
            else:
                score1 += player1[i]

        for i in range(len(player2)):
            if i > 0 and player2[i-1] == 10:
                score2 += player2[i] * 2
            elif i > 1 and player2[i-2] == 10:
                score2 += player2[i] * 2
            else:
                score2 += player2[i]

        if score1 > score2:
            return 1
        elif score1 < score2:
            return 2
        else:
            return 0