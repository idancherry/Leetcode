class Solution(object):
    def strStr(self, haystack, needle):
        l_needle=len(needle)
        l_haystack=len(haystack)
        for i in range(l_haystack-l_needle+1):
            if needle==haystack[i:i+l_needle]:
                return i
        return -1
