class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        num=[]
        p=0
        for i in nums:
            if i!=val:
                num.append(i)
            else:
                p+=1
        nums[:]=num
        return (len(nums))