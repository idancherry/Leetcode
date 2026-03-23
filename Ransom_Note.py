class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dic={}
        for i in magazine:
            dic[i]=dic.get(i,0)+1
        for i in ransomNote:
            if i in dic.keys() and dic[i]>0:
                dic[i]-=1
            else:
                return False
        return True