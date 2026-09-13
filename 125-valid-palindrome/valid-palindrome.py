class Solution(object):
    def isPalindrome(self, s):
        ans = "" 
        for i in s:
            if i.isalnum():
                ans += i.lower()
        return ans == ans[::-1]
        

        
        