import math
import itertools

# converts lists of strings to list of integers
def StrListToInt(l):
    return [int(x) for x in l]

#split list / string to equal pieces
def SplitByNumber(a, n):
    return [a[i:i+n] for i in range(0, len(a), n)]

#gets the row index by the tile index
def RowByIndex(index, board):
    row_index = int(index/9)
    return SplitByNumber(board, 9)[row_index]

#gets the column index by the tile index
def ColumnByIndex(index, board):
    column_index = index%9
    columns = SplitByNumber([row[i] for i in range(0,9) for row in SplitByNumber(board,9)], 9)
    return columns[column_index]

#gets the square index by the tile index
def SquareByIndex(index, board):
    square_index = math.floor(index/3)%3 + math.floor(index/27)*3
    squares = [[] for _ in range(9)]
    for x in range(0,81):
        squares[math.floor(x/3)%3 + math.floor(x/27)*3].append(board[x])
    
    return squares[square_index]

# check if it is possible to place the digit n in the tile
def CheckTile(index, n, board):
    if n not in StrListToInt(RowByIndex(index, board)):
        if n not in StrListToInt(ColumnByIndex(index,board)):
            if n not in StrListToInt(SquareByIndex(index,board)):
                return True
    return False

#check if there are duplicates in a list
def checkDuplicates(numbers):
    for i in range(0,len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i] == numbers[j]:
                if numbers[i]!=0 or numbers[j]!=0:
                    return True
    return False

#checks if the board is solveable
def validateBoard(board):
    rows = SplitByNumber(board, 9)
    columns = SplitByNumber([row[i] for i in range(0,9) for row in SplitByNumber(board,9)], 9)
    squares = [[] for _ in range(9)]
    for x in range(0,81):
        squares[math.floor(x/3)%3 + math.floor(x/27)*3].append(board[x]) 

    for numbers in itertools.chain(rows,columns,squares):
        if(checkDuplicates(numbers)):
            return True

    return False


#translates an rgb tuple of int to a tkinter friendly color code (HEX)
def toHex(rgb):
    return "#%02x%02x%02x" % rgb 

#gets unsolved soduku board as a list and returns the solved board
def Solve(board):
    board = [int(x) for x in board]
    solved_board = board.copy()
    
    #checks if the board is solveable
    if (validateBoard(board)):
        print("Invalid Board")
        return False

    index = 0
    while index < 81:  
        if board[index] == 0: # if the tile is placeable
            digitBeforeChange = solved_board[index]
            for x in range(solved_board[index] + 1, 10): # check which digit it can place in the tile
                if CheckTile(index, x, solved_board):
                    solved_board[index] = x
                    break
            if solved_board[index] != 0 and digitBeforeChange != solved_board[index]: # if the tile changed it moves one
                index += 1
            else: # if the tile didn't it goes to the last placeable tile
                solved_board[index] = 0
                index -= 1
                while board[index] != 0:
                    index -= 1
        else:
            index += 1 # if the tile isn't placeable it moves on
    return solved_board

