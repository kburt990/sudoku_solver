import pygame
import sys
import sudoku_logic

class sudokuSolver:
    def __init__(self):
        self.sudoku=sudoku_logic.sudoku()

    def draw_display(self):

        screen=pygame.display.set_mode((900,900))
        screen.fill((255,255,255)) #white screen

        line_color=(0,0,0) #rgb value for line_color (black)

        for i in range(9): #draw grid
            if i==3 or i==6: #draw thicker lines for visibility
                pygame.draw.line(pygame.display.get_surface(), line_color, (100 * i, 0), (100 * i, 900),3)
                pygame.draw.line(pygame.display.get_surface(), line_color, (0, 100 * i), (900, 100 * i),3)

            else:
                pygame.draw.line(pygame.display.get_surface(), line_color, (100 * i, 0), (100 * i, 900))
                pygame.draw.line(pygame.display.get_surface(), line_color, (0, 100 * i), (900, 100 * i))

        x, y = pygame.mouse.get_pos()
        self.draw_red_square(x, y)


        self.draw_numbers()




        pygame.display.flip()


    def draw_numbers(self) ->None:
        # fill grid with numbers
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 80)
        screen=pygame.display.get_surface()
        for row in range(9):
            for col in range(9):
                if(self.sudoku.board[row][col]!=0):
                    text_surface=font.render(f'{self.sudoku.board[row][col]}',False,(0,0,0))
                    screen.blit(text_surface,(30+100*col,9+100*row))




    def draw_red_square(self,x:int,y:int):

        #get which square coords belong to
        sq_x = int(x / 100)
        sq_y = int(y / 100)
        #print(f'({x},{y}) ({sq_x},{sq_y})')
        surface=pygame.display.get_surface()
        #get coords for rect object based off of mouse coords
        x1=100*sq_y
        y1=100*sq_x
        x2=x1+99
        y2=y1+99


        pygame.draw.rect(surface,(255,0,0),(y1,x1,100,100))



    def run(self):
        while True:
            self.draw_display()
            if(self.check_exit()):
                pygame.quit()
                break
            self.handle_events()


    def check_exit(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.sudoku.print_board()
            return True
        else:
            return False

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:
                x,y=pygame.mouse.get_pos()
                self.change_number(x,y)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.ui_solve()




    def change_number(self,x:int,y:int):
        sq_x = int(x / 100)
        sq_y = int(y / 100)
        while True:
            for event in pygame.event.get():
                #TODO FIND A BETTER WAY TO DO THIS
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    print(f'({x},{y}) ({sq_x},{sq_y})')
                    self.sudoku.add_num(sq_y,sq_x,1)
                    return

                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    print(f'({x},{y}) ({sq_x},{sq_y})')
                    self.sudoku.add_num(sq_y,sq_x,2)
                    return

                if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    print(f'({x},{y}) ({sq_x},{sq_y})')
                    self.sudoku.add_num(sq_y,sq_x,3)
                    return

                if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                    print(f'({x},{y}) ({sq_x},{sq_y})')
                    self.sudoku.add_num(sq_y,sq_x,4)
                    return

                if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                    print(f'({x},{y}) ({sq_x},{sq_y})')
                    self.sudoku.add_num(sq_y,sq_x,5)
                    return

                if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
                    print(f'({x},{y}) ({sq_x},{sq_y})')
                    self.sudoku.add_num(sq_y,sq_x,6)
                    return

                if event.type == pygame.KEYDOWN and event.key == pygame.K_7:
                    print(f'({x},{y}) ({sq_x},{sq_y})')
                    self.sudoku.add_num(sq_y,sq_x,7)
                    return

                if event.type == pygame.KEYDOWN and event.key == pygame.K_8:
                    print(f'({x},{y}) ({sq_x},{sq_y})')
                    self.sudoku.add_num(sq_y,sq_x,8)
                    return

                if event.type == pygame.KEYDOWN and event.key == pygame.K_9:
                    print(f'({x},{y}) ({sq_x},{sq_y})')
                    self.sudoku.add_num(sq_y,sq_x,9)
                    return

                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE: #DELETE ENTRY
                    print(f'({x},{y}) ({sq_x},{sq_y})')
                    self.sudoku.remove_num(sq_y,sq_x)
                    return


    def ui_solve(self):
        '''Modified solve in order to work with UI'''
        # backtracing to find valid solution for filled in returns true if
        coords = self.sudoku.find_empty()
        if coords == (-1, -1):  # default value to indicate no more empty slots
            return True
        row = coords[0]
        col = coords[1]
        for i in range(1, 10):
            if (self.sudoku.check_entry(row, col, i)):
                self.sudoku.board[row][col] = i
                self.draw_display()
                if (self.ui_solve()):
                    return True
            self.sudoku.board[row][col] = 0

        return False









if __name__=="__main__":
    su=sudokuSolver()
    su.run()