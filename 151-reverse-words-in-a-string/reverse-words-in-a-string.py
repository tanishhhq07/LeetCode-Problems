class Solution(object):
    def reverseWords(self, s):
        rev = s.split()
        rev.reverse()
        return " ".join(rev)
             