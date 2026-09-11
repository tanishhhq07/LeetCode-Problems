class Solution(object):
    def sortVowels(self, s):
        vowels = ['U','O','I','E','A','u','o','i','e','a']
        arr = []
        s = list(s)
        j = 0
        for i in s:
            if i in vowels:
                arr.append(i)

        arr.sort()
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = arr[j]
                j += 1

        return ''.join(s)