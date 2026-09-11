class Solution(object):
    def sortVowels(self, s):
        vowels = "AEIOUaeiou"
        count = [0] * 10
        s = list(s)
        j = 0
        for ch in s:
            if ch in vowels:
                count[vowels.index(ch)] += 1

        for i in range(len(s)):
            if s[i] in vowels:
                while count[j] == 0:
                    j += 1
                s[i] = vowels[j]
                count[j] -= 1

        return ''.join(s)