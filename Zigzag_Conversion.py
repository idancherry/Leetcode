class Solution(object):
    def convert(self, s, numRows):
        if numRows==1:
            return s
        lst=[""]*numRows
        ls=list(s)
        row=0
        down=True
        for i in ls:
            lst[row]+=i
            if row==numRows-1:
                down=False
            elif row==0:
                down=True
            if down:
                row+=1
            else:
                row-=1
        fin=""
        for i in lst:
            fin+=i
        return fin