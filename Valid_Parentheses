class Solution(object):
    def isValid(self, s):
        dic={"(":")","[":"]","{":"}"}
        l=list(s)
        if (len(l)%2==1):
            return False
        t=[]
        for i in l:
            if i in dic.keys():
                t.append(i)
                continue
            if not t or i in dic.values() and dic[t[-1]]!=i:
                return False
            t.pop()    
        if not t: return True
        return False