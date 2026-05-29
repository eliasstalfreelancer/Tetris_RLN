from engine.game import Game
from engine.colors import Colors
import pygame as pg
class Render:
    def __init__(self):
        self.title_font = pg.font.Font(None, 40)

        self.score_text_cord = (365,20,50,50)
        self.next_text_cord = (376,180,50,50)
        self.level_text_cord = (376,460,50,50)
        self.rect_box_cord = (320,450,50,50)

        self.score_surface = self.title_font.render("Score", True, Colors.white,) #score text

        self.next_surface = self.title_font.render("Next", True, Colors.white) #next text

        self.level_surface = self.title_font.render("Level", True,Colors.white) #Level text

        self.game_over_surface = self.title_font.render("Game over", True, Colors.white) #game over text

        self.score_rect = pg.Rect(320,55,170,60) #defining the score box

        self.next_rect = pg.Rect(320,215,170,180) #defining the next box

        self.level_rect = pg.Rect(320,495,170,60) #defining the level box

    
    
    def background(self,screen):
        screen.fill(Colors.dark_blue) #Background
    
    def score_vaule_render(self,screen, score):
        score_counter = self.title_font.render(str(score), True, Colors.white) #score vaule 
        screen.blit(score_counter,score_counter.get_rect(centerx = self.score_rect.centerx,centery = self.score_rect.centery))

    def level_vaule_render(self,screen,level):
        level_counter =  self.title_font.render(str(level), True, Colors.white) #Level vaule
        screen.blit(level_counter,level_counter.get_rect(centerx = self.level_rect.centerx,centery = self.level_rect.centery))
    
    def level_box(self,screen):
        pg.draw.rect(screen,Colors.light_blue,self.level_rect,0,10) #level box

    def score_text(self,screen):
        screen.blit(self.score_surface,self.score_text_cord)#score text
    
    def next_text(self,screen):
        screen.blit(self.next_surface,self.next_text_cord )#next text
    
    def level_text(self,screen):
        screen.blit(self.level_surface,self.level_text_cord)#level text
    
    def game_over_text(self,screen):
        screen.blit(self.game_over_surface,self.rect_box_cord)#gameover text
    
    def score_box(self,screen):
        pg.draw.rect(screen,Colors.light_blue,self.score_rect,0,10)#score box
    
    def next_box(self,screen):
        pg.draw.rect(screen,Colors.light_blue,self.next_rect,0,10)#next box
    
def render_game(screen,game):
        render = Render()
        
        render.background(screen)
        render.score_text(screen)
        render.next_text(screen)
        if game.game_over == True:
            render.game_over_text(screen)
        render.score_box(screen)
        render.score_vaule_render(screen,game.score)
        render.next_box(screen)
        render.level_box(screen)
        render.level_vaule_render(screen,game.level)
        game.draw(screen)
        pg.display.update()