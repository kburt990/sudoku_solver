class sudoku: #represents standard 9x9 sudoku board
    def __init__(self):
        self.board=self.create_board()

    def create_board(self): #set up 9x9 board for standard game
        board=[]
        for i in range(9):
            board.append([0,0,0,0,0,0,0,0,0]) #fill board with default values
        return board

    def add_num(self,row:int, col:int, val:int):
        self.board[row][col]=val

    def remove_num(self,row:int, col:int):
        if(self.board[row][col]!=0):
            self.board[row][col]=0 # reset to default value
        else:
            print("ERROR: ATTEMPTING TO REMOVE FROM EMPTY ELEMENT")

    def print_board(self)->None:

        for row in self.board:
            for column in row:
                if column!=0:
                    print(column,end=' ')
                else:
                    print("X",end=' ') #empty
            print()



    def check_row(self, row:int, col:int,num:int)->bool:
    #checks to see if there is a duplicate number in row

        if num==0:
            return False
        for i in range(9):
            if self.board[row][0+i]==num and 0+i!=col:
                return False
        return True






    def check_col(self, row:int, col:int,num:int)->bool:
    #checks to see if there is a duplicate number in col

        if num == 0:
            return False
        for i in range(9):
            if self.board[0+i][col] == num and 0+i != row:
                return False
        return True

    def check_sq(self, row:int, col:int,num:int)->bool: #checks to see if entry is valid relative to the square surrounding it

        #check bounds, should be optimized later
        if(num == 0):
            return False
        row_start=0
        col_start=0
        if 3<=row<6:
            row_start=3
        if row>=6:
            row_start=6

        if 3<=col<6:
            col_start=3
        if col>=6:
            col_start=6

        for i in range(row_start,row_start+3):
            for j in range(col_start,col_start+3):
                if self.board[i][j] == num:
                    return False

        return True


    def check_entry(self,row:int,col:int,num:int)->bool:
        #checks to see if number is valid entry
        if self.check_row(row,col,num) and self.check_col(row,col,num) and self.check_sq(row,col,num):
            return True
        else:
            return False



    def find_empty(self)->tuple: #returns first empty element in board
        for row in range(9):
            for col in range(9):
                if self.board[row][col]==0:
                    return (row,col)
        return (-1,-1) #default value to indicate no more empty slots

    def solve(self)->bool:
        #backtracing to find valid solution for filled in returns true if
        coords = self.find_empty()
        if coords==(-1,-1) : #default value to indicate no more empty slots
            return True
        row=coords[0]
        col=coords[1]
        for i in range(1,10):
            if(self.check_entry(row,col,i)):
                self.board[row][col]=i
                if(self.solve()):
                    return True
            self.board[row][col]=0
        return False

































if __name__=="__main__":
    board = sudoku()
    # board.add_num(0,0,1)
    # board.add_num(0, 1, 2)
    # board.add_num(0, 2, 3)
    # board.add_num(1, 0, 4)
    # board.add_num(1, 1, 5)
    # board.add_num(1, 2, 6)
    # board.add_num(2, 0,8)
    # board.add_num(2, 1, 7)
    # board.add_num(2, 2, 9)

    board.add_num(0, 2, 2)
    board.add_num(0, 6, 8)
    board.add_num(1, 1, 5)
    board.add_num(1, 2, 9)
    board.add_num(1, 5, 1)
    board.add_num(1, 6, 6)
    board.add_num(1, 8, 7)
    board.add_num(2, 3, 4)
    board.add_num(2, 5, 3)
    board.add_num(3, 2, 4)
    board.add_num(3, 4, 5)
    board.add_num(3, 6, 2)
    board.add_num(3, 7, 6)
    board.add_num(3, 8, 9)
    board.add_num(4, 3, 6)
    board.add_num(4, 4, 3)
    board.add_num(4, 5, 7)
    board.add_num(4, 7, 5)
    board.add_num(4, 8, 4)
    board.add_num(6, 0, 8)
    board.add_num(6, 2, 6)
    board.add_num(6, 6, 4)
    board.add_num(7, 3, 3)
    board.add_num(8, 3, 2)
    board.add_num(8, 5, 9)
    board.add_num(8, 8, 1)
    board.print_board()
    print()
    print(board.solve())
    board.print_board()









