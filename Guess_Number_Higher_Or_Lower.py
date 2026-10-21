class Solution(object):
    def guessNumber(self, n):
        l=1
        r=n
        while r>l:
            if r-l==1:
                if guess(r)==0: return r
                elif guess(l)==0: return l
            mid = l+ (r-l)//2
            g = guess(mid)
            if g==0: return mid
            elif g==-1:
                r=mid
            else:
                l=mid
        return 1