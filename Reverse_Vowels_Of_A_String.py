class Solution(object):
    def reverseVowels(self, s):
        l=[]
        s = list(s)
        vowels = set(["a","A","e","E","o","O","U","u","i","I"])
        for i in range(len(s)):
            if s[i] in vowels:
                l.append(i)
        length = len(l)
        for i in range(length//2):
            temp = s[l[i]]
            s[l[i]] = s[l[length-i-1]]
            s[l[length-i-1]] = temp
        return ''.join(s)