class Solution(object):
    def intToRoman(self, num):
        s=""
        nums=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        symbols=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        i=0
        while num>0:
            if num>nums[i]-1:
                num-=nums[i]
                s+=symbols[i]
            else:
                i+=1
        return s
        