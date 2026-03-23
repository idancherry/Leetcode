class Solution(object):
    def longestConsecutive(self, nums):
        s=set(nums)
        m=0
        for i in s:
            if not i-1 in s:
                c=1
                next=i+1
                while next in s:
                    c+=1
                    next+=1
                m=max(m,c)
        return m