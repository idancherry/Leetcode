class Solution(object):
    def nextPermutation(self, nums):
        i=len(nums)-2
        while (i>-1 and nums[i]>=nums[i+1]):
            i-=1
        ind=len(nums)-1
        while (ind>-1 and nums[ind]<=nums[i]):
            ind-=1
        temp=nums[ind]
        nums[ind]=nums[i]
        nums[i]=temp
        
        nums[i+1:]=sorted(nums[i+1:])