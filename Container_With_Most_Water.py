class Solution(object):
    def maxArea(self, height):
        L=0
        R=len(height)-1
        m=0
        for i in range(len(height)):
            vol=(R-L)*min(height[R],height[L])
            if vol>m:
                m=vol
            if height[L]>height[R]:
                R-=1
            else:
                L+=1
        return m