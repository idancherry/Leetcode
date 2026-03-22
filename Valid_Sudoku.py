class Solution(object):
    def isValidSudoku(self, board):
        for row in board:
            count=[0]*9
            for i in range(9):
                if row[i]!=".":
                    ind=int(row[i])-1
                    count[ind]+=1
                    if count[ind]>1:
                        return False
        for col in range(9):
            count=[0]*9
            for row in board:
                if row[col]!=".":
                    ind=int(row[col])-1
                    count[ind]+=1
                    if count[ind]>1:
                        return False
        for row in range(3):
            for col in range(3):
                count=[0]*9
                for i in range(3):
                    for j in range(3):
                        if board[row*3+i][col*3+j]!=".":
                            ind=int(board[row*3+i][col*3+j])-1
                            count[ind]+=1
                            if count[ind]>1:
                                return False

        return True