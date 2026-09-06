class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        vowels = "aeiou"
        count = 0
        for ch in s[0]:
            if ch in vowels:
                count += 1

        for i in range(1, len(s)):
            temp = 0
            for ch in s[i]:
                if ch in vowels:
                    temp += 1
            if temp == count:
                s[i] = s[i][::-1]
                
        return " ".join(s)