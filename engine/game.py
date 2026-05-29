from engine.grid import Grid
from engine.blocks import *
import random
import math

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [OBlock(),IBlock(),JBlock(),LBlock(),SBlock(),TBlock(),ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.level = 1
        self.line_tracker = 0
        self.frames_per_sec = 60
        self.game_speed = int(1000/(self.frames_per_sec*(0.0088 * (math.e ** (0.3532 * self.level)))))# game_speed = 0.0088e^0.3532*level
        self.fall_timer = 0
    

    def update_score(self,line_cleared,level,move_down_points):
        if line_cleared == 1:
            self.score += 40*(level+1)# 40*(level +1) for one line clear
        elif line_cleared ==2 :
            self.score += 100*(level+1) # 100*(level +1) for two line clear
        elif line_cleared == 3: 
            self.score += 300*(level+1) # 300*(level +1) for three line clear
        elif line_cleared == 4:
            self.score += 400*(level+1) # 400*(level +1) for one line clear
        self.score += move_down_points
    
    def update(self, dt):

        if self.game_over:
            return

        self.fall_timer += dt

        if self.fall_timer >= self.game_speed:

            self.fall_timer = 0

            self.move_down()

    def update_level(self, line_cleared):
        
        self.line_tracker += line_cleared
        if line_cleared > 0:
            print(self.line_tracker)
            if self.line_tracker == 10:
                self.level += 1
                self.game_speed = int(1000*self.frames_per_sec*(0.0088 * (math.e ** (0.3532 * self.level))))
                self.line_tracker = 0
                
        


    def get_random_block(self):

        if len(self.blocks) == 0:
                self.blocks = [OBlock(),IBlock(),JBlock(),LBlock(),SBlock(),TBlock(),ZBlock()]
        
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
         self.current_block.move(0,-1)
         if self.block_inside() == False or self.block_fits() == False:
              self.current_block.move(0,1)
    
    def move_right(self):
         self.current_block.move(0,1)
         if self.block_inside() == False  or self.block_fits() == False:
              self.current_block.move(0,-1)
    
    def move_down(self):
        self.current_block.move(1,0)
        if self.block_inside() == False or self.block_fits() == False: 
              self.current_block.move(-1,0)
              self.lock_block()


    def prefrom_action(self,action):
        if action == 0:
            self.move_left()

        elif action == 1:
            self.move_right()

        elif action == 2:
            self.rotate()

        elif action == 3:
            self.move_down()

        

    def lock_block(self):
        # make the block 
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block =  self.next_block
        self.next_block = self.get_random_block()
        rows_cleared =self.grid.clear_full_rows( )
        self.update_level(rows_cleared)
        self.update_score(rows_cleared,self.level,0)
        
        
        if self.block_fits() == False:
            self.game_over = True

    def reset(self):
        self.grid.reset()
        self.blocks = [OBlock(),IBlock(),JBlock(),LBlock(),SBlock(),TBlock(),ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.level = 1
        self.line_tracker = 0
        self.game_speed = 1000*self.frames_per_sec*(0.0088 * (math.e ** (0.3532 * self.level)))

    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row,tile.column) == False:
                return False
             
        return True

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()


    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row,tile.column) == False:
                return False
        return True
    
    def draw(self, screen):
         self.grid.draw(screen,11,11)
         self.current_block.draw(screen,11,11)
         self.next_block.draw(screen,270,270)



         