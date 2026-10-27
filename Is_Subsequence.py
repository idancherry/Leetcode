class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s: return True
        i=0
        j=0
        while j<len(t) and i<len(s):
            if s[i]==t[j]:
                if i+1==len(s): return True
                i+=1
            j+=1
        return False