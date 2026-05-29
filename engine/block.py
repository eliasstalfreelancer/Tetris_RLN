from engine.colors import Colors
import pygame as pg
from engine.position import *

#class for drawing the blocks
class Block:
    
    def __init__(self,id):
        self.id = id #colour
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset= 0
        self.rotation_sate = 0
        self.colors = Colors.get_cell_colors()

    def move(self,rows,columns):
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self):
        tiles = self.cells[self.rotation_sate]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset,
                                position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles
    
    def draw(self,screen,x_offset,y_offset):
        tiles = self.get_cell_positions()# takes from potions information from the blocks and adds the offset to moved the tiles but them in a 
        # list on where to draw them 
        for tile in tiles:
            tile_rect = pg.Rect(tile.column * self.cell_size +x_offset, tile.row *self.cell_size +y_offset,
            self.cell_size-1 ,self.cell_size-1 )
            pg.draw.rect(screen,self.colors[self.id],tile_rect)

    def rotate(self):
        self.rotation_sate += 1
        if self.rotation_sate == len(self.cells):
            self.rotation_sate = 0

    def undo_rotation(self):
        self.rotation_sate -= 1
        if self.rotation_sate == 0:
            self.rotation_sate = len(self.cells) - 1 