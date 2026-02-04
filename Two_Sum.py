class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a=dict()
        for i in range(len(nums)):
            if nums[i] in a:
                return [a[nums[i]],i]
            else:
                a[target-nums[i]]=i
