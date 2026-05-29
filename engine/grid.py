import pygame as pg
from engine.colors import Colors
class Grid:
    def __init__(self):
        #---playing area----
        # number of cells in height of playing area
        self.num_rows = 20
        # number of cells in widtht of playing area
        self.num_cols = 10
        # size of cell in pixels
        self.cell_size = 30
        # playing area array
        self.grid = [[ 0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        # colors
        self.colors = Colors.get_cell_colors()

    

    
    def print_grid(self):
        #Displays current array 
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end= " ")
            print()

    def is_inside(self,row,column): 
        #checks if the block is inside the boundery of the game or inside a block
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    def is_empty(self,row,column):
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self,row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def clear_row(self,row):
        for column in range(self.num_cols):
             self.grid[row][column] = 0

    def move_row_down(self,row,num_rows):
        for column in range(self.num_cols):
            self.grid[row+num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0
    
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row,completed)
        return completed
                 
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def draw(self,screen,offset_x,offset_y):

        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_vaule = self.grid[row][column]
                cell_rect = pg.Rect(offset_x + column*self.cell_size,offset_y + row*self.cell_size,
                                    self.cell_size-1,self.cell_size-1)
                pg.draw.rect(screen,self.colors[cell_vaule],cell_rect)
    
