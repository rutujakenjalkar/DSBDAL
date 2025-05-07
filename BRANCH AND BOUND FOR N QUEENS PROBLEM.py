#BRANCH AND BOUND FOR N QUEENS PROBLEM

global boardsize  #boardsize variable can be accessed anywhere 
boardsize=5

def printSolution(boardsize):
    for i in range(boardsize):
        for j in range(boardsize):
            print(board[i][j]," ")
        print()


def issafe(board,row,col):
    #To check whether the queen is present in for all collumns of a particular row
    for i in range(col):
        if board[row][i] == 1:
            return False
        
    #To check the presence of the queen in the upper diagonal element from a particular positon on the board 
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    #To check whether of the queen in the lower diagonal elemnent from a particular position on the board 
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True



