class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        partner = [0] * n
        for a, b in pairs:
            partner[a] = b
            partner[b] = a
        unhappy = 0
        for x in range(n):
            y = partner[x]
            for u in preferences[x]:
                if u == y:
                    break
                v = partner[u]
                if preferences[u].index(x) < preferences[u].index(v):
                    unhappy += 1
                    break
        return unhappy
        