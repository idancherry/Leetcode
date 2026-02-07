class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min=1e15
        max=-1
        for i in prices:
            if i<min:
                min=i
            if i-min>max:
                max=i-min
        return max        