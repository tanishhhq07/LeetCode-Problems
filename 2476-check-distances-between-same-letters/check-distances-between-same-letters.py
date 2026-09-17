class Solution(object):
    def checkDistances(self, s, distance):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        seen = {}
        for i in range(len(s)):
            if s[i] in seen:
                index = alphabet.index(s[i])

                if i - seen[s[i]] - 1 != distance[index]:
                    return False
            else:
                seen[s[i]] = i

        return True