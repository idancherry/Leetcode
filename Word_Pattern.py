class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        d={}
        l=s.split()
        if len(pattern)!=len(l):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d.keys():
                if d[pattern[i]]!=l[i]:
                    return False
            else:
                if l[i] in d.values():
                    return False
                d[pattern[i]]=l[i]
        return True
        