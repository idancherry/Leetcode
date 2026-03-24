class Solution(object):
    def findMin(self, nums):
        L,R=0, len(nums)-1
        while L<R:
            m=(R+L)//2
            
            if nums[m]>nums[R]:
                L=m+1
            else:
                R=m
            
        return nums[L]