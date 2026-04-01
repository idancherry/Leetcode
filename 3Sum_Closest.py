class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        summ=float('inf')
        i=0
        while i<len(nums)-2:
            l, r = i+1,len(nums)-1
            while l<r:
                curr=nums[i]+nums[r]+nums[l]
                if abs(target-curr)<abs(target-summ):
                    summ=(curr)
                if curr==target:
                    return target
                elif curr<target:
                    l+=1
                else:
                    r-=1
            i+=1
        return summ