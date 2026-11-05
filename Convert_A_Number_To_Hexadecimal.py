class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        i=0
        s=""
        letters = ["a", "b", "c", "d", "e", "f"]
        if num<0:
            num+=2**32
        if num==0: return "0"
        while 16**(i+1)<=num:
            i+=1

        while num>0:
            pow = 16**i
            r = num % pow
            div = num // pow
            if div>9:
                s+=letters[div-10]
            else:
                s+=str(div)
            i-=1
            num = r
        while i>=0:
            s+="0"
            i-=1
        return s