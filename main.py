import pygame as pg
import sys
from engine.game import Game
from engine.colors import Colors
from engine.render import *
from engine.position import Position
import time
from engine.grid import Grid



#to start pygame
pg.init()
# ----Definitions----
# creates the windows and sets the resolutions to 300x600
screen = pg.display.set_mode((500,620))
# set the window names to tetris
pg.display.set_caption("Tetris")

# framerate variable 
clock = pg.time.Clock()
game = Game()
render = Render()
grid = Grid()
model_best_score = 0
# Game loop
while True:

    dt = clock.tick(60)

    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:

            if event.key == pg.K_LEFT:
                game.preform_action(0)

            if event.key == pg.K_RIGHT:
                game.preform_action(1)

            if event.key == pg.K_UP:
                game.preform_action(2)

            if event.key == pg.K_DOWN:
                game.preform_action(3)
    
    
    # UPDATE GAME
    game.update(dt)
    
    # render
    render_game(screen,game)
  
    
    

    