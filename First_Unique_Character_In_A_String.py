class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars=set()
        for i in range(len(s)):
            if s[i] in chars:
                continue
            else:
                if s.count(s[i])==1:
                    return i
                chars.add(s[i])
                                
        return -1