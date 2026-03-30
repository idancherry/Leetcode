class Solution(object):
    def getRow(self, rowIndex):
        pascal=[[1],[1,1]]
        for i in range(2,rowIndex+1):
            res=[1]*(i+1)
            for j in range(1,i):
                res[j]=pascal[i-1][j-1]+pascal[i-1][j]
            pascal.append(res)
        return pascal[rowIndex]