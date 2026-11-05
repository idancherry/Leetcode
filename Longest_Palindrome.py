class Solution(object):
    def longestPalindrome(self, s):
        d ={}
        res=0
        for i in s:
            if i not in d.keys():
                d[i]=1
            else:
                if d[i]==1:
                    res+=2
                    d[i]=0
                else:
                    d[i]=1
        for i in d.keys():
            if d[i]==1:
                return res+1
        return res