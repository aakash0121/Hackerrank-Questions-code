class Sudoku(object):
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def printSudoku(self):
        for r in range(9):
            for c in range(9):
                print(self.sudoku[r][c], end = " ")
            print()

    def check_in_row(self, row, col, num):
        for c in range(9):
            if (self.sudoku[row][c] == num):
                return True
        return False
    
    def check_in_col(self, row, col, num):
        for r in range(9):
            if (self.sudoku[r][col] == num):
                return True
        return False

    def check_in_box(self, row, col, num):
        for i in range(3):
            for j in range(3):
                if self.sudoku[i+row][j+col] == num:
                    return True
        return False
    
    def find_next_empty_cell(self, l):
        for r in range(9):
            for c in range(9):
                if self.sudoku[r][c] == 0:
                    l[0] = r
                    l[1] = c
                    return True
        return False
    
    def check_location_is_Safe(self, row, col, num):
        if not self.check_in_box(row-row%3, col-col%3, num) and not self.check_in_row(row, col, num) and not self.check_in_col(row, col, num):
            return True
        return False
    
    def sudoku_solve(self):
        l = [0,0]
        #self.printSudoku()

        if not self.find_next_empty_cell(l):
            return True
        
        row = l[0]
        col = l[1]
        #print(row, col)

        for num in range(1, 10):
            if (self.check_location_is_Safe(row, col, num)):
                self.sudoku[row][col] = num
            
                if self.sudoku_solve():
                    return True
                
                self.sudoku[row][col] = 0
        
        return False

if __name__ == "__main__":
    grid=[[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]] 
    
    sudoku = Sudoku(grid)
    
    if sudoku.sudoku_solve(): 
        sudoku.printSudoku() 
    else: 
        print("No solution exists")