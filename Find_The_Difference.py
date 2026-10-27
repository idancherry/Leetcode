class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        set1=set(s)
        set2=set(t)
        diff = set2-set1
        if diff:
            for i in diff:
                return i 
        for i in set1:
            if s.count(i)!=t.count(i):
                return i