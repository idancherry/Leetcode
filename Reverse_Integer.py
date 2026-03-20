class Solution(object):
    def reverse(self, x):
        pos=(x>0)
        x=abs(x)
        x=int(str(x)[::-1])
        if x>2147483647 or x<-2147483648:
            return 0
        if not pos:
            return -x
        return x