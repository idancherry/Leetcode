class Solution(object):
    def reverseBits(self, n):
        res=0
        for i in range(32):
            fact=2**(31-i)
            if n>=fact:
                res+=2**i
                n-=fact
        return res