import math

class Solve:
    def StrListToInt(self, l):
        return [int(x) for x in l]
    
    def SplitByNumber(self, a, n):
        return [a[i:i+n] for i in range(0, len(a), n)]
    
    def RowByIndex(self, index, board):
        row_index = int(index/9)
        return self.SplitByNumber(board, 9)[row_index]

    def ColumnByIndex(self, index, board):
        column_index = index%9
        columns = self.SplitByNumber([row[i] for i in range(0,9) for row in self.SplitByNumber(board,9)], 9)
        return columns[column_index]

    def SquareByIndex(self, index, board):
        square_index = math.floor(index/3)%3 + math.floor(index/27)*3
        squares = [[] for _ in range(9)]
        for x in range(0,81):
            squares[math.floor(x/3)%3 + math.floor(x/27)*3].append(board[x])
        
        return squares[square_index]
        
    def CheckTile(self, index, n, board):
        if n not in self.StrListToInt(self.RowByIndex(index, board)):
            if n not in self.StrListToInt(self.ColumnByIndex(index,board)):
                if n not in self.StrListToInt(self.SquareByIndex(index,board)):
                    return True
        return False

