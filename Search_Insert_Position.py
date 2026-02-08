class Solution(object):
    def searchInsert(self, nums, target):
        L,R=0,len(nums)-1
        while L<=R:
            mid=L+(R-L)//2
            if nums[mid]==target:
                return mid
            if R-L==1 and nums[R]==target:
                return R
            elif nums[mid]<target:
                L=mid+1
            else:
                R=mid-1
        return L