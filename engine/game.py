from engine.grid import Grid
from engine.blocks import *
from engine.block import *
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
        self.line_tracker_for_level = 0
        self.line_tracker_for_ai = 0
        self.frames_per_sec = 60
        self.game_speed = int(1000/(self.frames_per_sec*(0.0088 * (math.e ** (0.3532 * self.level)))))# game_speed = 0.0088e^0.3532*level
        self.fall_timer = 0
        self.reward = 0
    
    def get_reward(self):
        return self.reward

    def get_state(self):

        temp_grid = [row[:] for row in self.grid.grid]

        tiles = self.current_block.get_cell_positions()

        for tile in tiles:

            if 0 <= tile.row < self.grid.num_rows and 0 <= tile.column < self.grid.num_cols:

                temp_grid[tile.row][tile.column] = self.current_block.id

        state = []

        for row in temp_grid:

            for cell in row:

                state.append(cell)

        return state

    
    def update_score(self,line_cleared,level,move_down_points):
        if line_cleared == 1:
            self.score += 40*(level+1)# 40*(level +1) for one line clear
            self.reward = 40*(level+1)
        elif line_cleared ==2 :
            self.score += 100*(level+1) # 100*(level +1) for two line clear
            self.reward = 100*(level+1)
        elif line_cleared == 3: 
            self.score += 300*(level+1) # 300*(level +1) for three line clear
            self.reward = 300*(level+1)
        elif line_cleared == 4:
            self.score += 400*(level+1) # 400*(level +1) for one line clear
            self.reward = 400*(level+1)
        self.score += move_down_points
        self.reward = move_down_points

    def simulation_update(self):

        self.move_down()

    def update(self, dt):

        if self.game_over:
            return

        self.fall_timer += dt

        if self.fall_timer >= self.game_speed:

            self.fall_timer = 0

            self.move_down()

    def update_level(self, line_cleared):
        
        self.line_tracker_for_level += line_cleared 
        if line_cleared > 0:

            if self.line_tracker_for_level == 10:
                self.level += 1
                self.game_speed = int(1000*self.frames_per_sec*(0.0088 * (math.e ** (0.3532 * self.level))))
                self.line_tracker_for_level = 0
                
                
        


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


    def preform_action(self,action):
        if action == 0:
            self.move_left()

        elif action == 1:
            self.move_right()

        elif action == 2:
            self.rotate()

        elif action == 3:
            self.update_score(0,0,1)
            self.move_down()

        

    def lock_block(self):
        # make the block 
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            #print(position.row, position.column)
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block =  self.next_block
        self.next_block = self.get_random_block()
        rows_cleared =self.grid.clear_full_rows( )
        self.update_level(rows_cleared)
        self.update_score(rows_cleared,self.level,0)
        self.line_tracker_for_ai += 1 #might change to soon to a better way on controlling this
    
        

        
        
        
        if self.block_fits() == False:
            self.game_over = True

    def reset(self):
        self.game_over = False
        self.grid.reset()
        self.blocks = [OBlock(),IBlock(),JBlock(),LBlock(),SBlock(),TBlock(),ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.level = 1
        self.line_tracker = 0
        self.score = 0
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



         