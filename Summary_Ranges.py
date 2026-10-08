class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res=[]
        length = len(nums)
        if length==0: return res
        if length==1: return [str(nums[0])]
        l=0
        r=1
        while r<length:
            if nums[r]-nums[r-1]==1:
                if r+1==length:
                    res.append(str(nums[l])+"->"+str(nums[r]))
                    return res
                else:
                    r+=1
            else:
                if r-1==l:
                    res.append(str(nums[l]))
                    l+=1
                    r+=1
                else:
                    res.append(str(nums[l])+"->"+str(nums[r-1]))
                    l=r
                    r+=1

            if r==length and r-l==1:
                res.append(str(nums[l]))
                break
        return res