class Solution(object):
    def romanToInt(self, s):
        vals1={"I":1,"V":5, "X":10,"L":50, "C":100,"D":500,"M":1000}
        vals2={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900,}
        i,sum=0,0
        while(i<len(s)):
            if len(s)-i>1 and s[i:i+2] in vals2:
                sum+=vals2[s[i:i+2]]
                i+=2
            elif s[i:i+1] in vals1:
                sum+=vals1[s[i:i+1]]
                i+=1
        return sum
