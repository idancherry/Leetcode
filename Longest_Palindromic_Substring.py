class Solution(object):
    def longestPalindrome(self, s):
        if s==s[::-1]:
            return s
        for i in range(len(s),0,-1):
            for j in range(len(s)-i+1):
                st=s[j:j+i]
                if (st==st[::-1]):
                    return st
        return s[0]