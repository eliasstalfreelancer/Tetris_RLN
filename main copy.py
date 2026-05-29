import pygame as pg
import sys
from engine.game import Game
from engine.colors import Colors
from engine.render import *
import time



#to start pygame
pg.init()
# ----Definitions----
# creates the windows and sets the resolutions to 300x600
screen = pg.display.set_mode((500,620))
# set the window names to tetris
pg.display.set_caption("Tetris")

# framerate variable 
clock = pg.time.Clock()
games = [Game() for _ in range(10)]
game = Game()
render = Render()
GAME_UPDATE = pg.USEREVENT
curent_speed = Game().game_speed
pg.time.set_timer(GAME_UPDATE,curent_speed)

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
                game.prefrom_action(0)

            if event.key == pg.K_RIGHT:
                game.prefrom_action(1)

            if event.key == pg.K_UP:
                game.prefrom_action(2)

            if event.key == pg.K_DOWN:
                game.prefrom_action(3)

    # UPDATE GAME
    for game in games:
        game.update(dt)

    # render
    render_game(screen)
    
    games[model_best_score].draw(screen)
    
    pg.display.update()

    