class Solution(object):
    def intersection(self, nums1, nums2):
        s = set(nums2)
        l=[]
        for i in nums1:
            if i in s:
                l.append(i)
                s.remove(i)
        return l