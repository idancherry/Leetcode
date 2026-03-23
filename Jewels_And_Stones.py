class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        s=set(jewels)
        count=0
        for i in stones:
            if i in s:
                count+=1
        return count