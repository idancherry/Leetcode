class Solution(object):
    def reverseString(self, s):
        L,R = 0, len(s)-1
        while L<R:
            s[R], s[L]= s[L], s[R]
            L+=1
            R-=1
        return s