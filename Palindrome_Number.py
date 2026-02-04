class Solution(object):
    def isPalindrome(self, x):
        st=list(str(x))
        l=len(st)
        if l<2: return True
        i=0
        while (i<l/2):
            if st[i]!=st[l-i-1]:
                return False
            i+=1
        return True

        