class Solution(object):
    def myAtoi(self, s):
        if s=="":
            return 0
        digits=[str(dig) for dig in range(10)]
        i=0
        while i<len(s):
            if s[i]!=" ":
                break
            i+=1
        s=s[i:]
        if s=="":
            return 0
        DEBUG=s=="-04f"
        neg=s[0]=="-"
        if neg or s[0]=="+":
            s=s[1:]
        i=0
        while i<len(s):
            if s[i]!="0":
                break
            i+=1
        s=s[i:]
        i=0
        while i<len(s):
            if not s[i] in digits:
                break
            i+=1
        if i<len(s):
            s=s[:i]       

        if s=="":
            return 0
        try:
            x=int(s)
        except:
            return 0
        if neg:
            x=-x
        if x>2147483647:
            return 2147483647
        elif x<-2147483648:
            return -2147483648
        return x