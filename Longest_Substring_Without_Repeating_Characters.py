class Solution(object):
    def lengthOfLongestSubstring(self, s):
        a=set()
        ls=list(s)
        l=0
        r=0
        m=0
        while r<len(ls):
            if not ls[r] in a:
                a.add(ls[r])
                r+=1
                if len(a)>m:
                    m=len(a)
            else:
                a.remove(ls[l])
                l+=1
        return m