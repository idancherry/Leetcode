class Solution(object):
    def isPerfectSquare(self, num):
        l=1
        r=num
        lsqr=1
        rsqr=num*num
        while r>l:
            mid = l+(r-l)//2
            mid_sqr = mid*mid
            if lsqr==num or rsqr==num or mid_sqr == num:
                return True
            if r-l==1: return False
            if mid_sqr>num:
                r=mid
                rsqr = mid_sqr
            else:
                l = mid
                lsqr = mid_sqr
        return num==1