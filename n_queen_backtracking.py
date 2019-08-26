class Backtracking(object):
    def __init__(self, n, board):
        self.board = board
        self.n = n

    def printBoard(self):
        return self.board
    
    def isSafe(self, row, col):
        for i in range(row):
            if self.board[i][col] == 1:
                return False
            
        for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[r][c] == 1:
                return False
            
        for r, c in zip(range(row, -1, -1), range(col, self.n, 1)):
            if self.board[r][c] == 1:
                return False
        return True
        
    def NQueen(self, row):
        if row >= self.n:
            return True
        
        for i in range(self.n):

            if self.isSafe(row, i):
                self.board[row][i] = 1
            
                if self.NQueen(row+1) == True:
                    return True
            
            self.board[row][i] = 0
        
        return False

if __name__ == "__main__":
    board = [ [0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0] 
             ] 
    n = len(board)
    
    queen = Backtracking(n, board)
    if queen.NQueen(0) == False:
        print("solution does not exist")
    else:
        print(f"solution exists: {queen.printBoard()}")
