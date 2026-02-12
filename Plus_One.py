class Solution(object):
    def plusOne(self, digits):
        i=len(digits)-1
        while(True):
            if i<0:
                digits.insert(0,1)
                break
            if digits[i]==9:
                digits[i]=0
                i-=1
            else:
                digits[i]+=1
                break
        return digits