import pygame as pg
import sys
from engine.grid import Grid
from engine.game import Game
from engine.colors import Colors
from engine.render import *
import time

class Tetris_gym:
    def __init__(self):
        pg.init()
        # ----Definitions----
        # creates the windows and sets the resolutions to 300x600
        self.screen = pg.display.set_mode((500,620))
        # set the window names to tetris
        pg.display.set_caption("Tetris")
        # framerate variable 
        self.clock = pg.time.Clock()
        self.game= Game()
        
        self.renderer = Render()
        self.model_best_score = 0

    def reset(self):
        self.game.reset()
        return self.game.get_state()
    
    def step(self,action):
        self.game.line_tracker_for_ai
        self.game.preform_action(action)
        self.game.simulation_update()
        state = self.game.get_state()
        reward = self.game.get_reward()
        linetracker = self.game.line_tracker_for_ai
        
        done = self.game.game_over

        return state, reward, done, 
    
    def render(self, render_delay = 0):
        time.sleep(render_delay)
        render_game(self.screen,self.game)
    
    def close(self):
        pg.quit()
        sys.exit()