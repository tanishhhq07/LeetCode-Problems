class Solution(object):
    def freqAlphabets(self, s):
        ans = []
        i = 0
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                num = int(s[i:i+2])
                i += 3
            else:
                num = int(s[i])
                i += 1

            ans.append(alphabet[num - 1])

        return ''.join(ans)