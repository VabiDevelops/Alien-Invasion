import pygame
from pygame.sprite import Sprite

class Goli(Sprite):
    ''' A class to manage goliya in game'''
    def __init__(self, ai_game):
        '''Create a goli object at the ship's current position'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.goli_color
        
        #create a goli rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.goli_width, self.settings.goli_height)
        self.rect.midtop = ai_game.rect.midtop
        
        #store the goli's position as a float
        self.y = float(self.rect.y)
        
    def update(self):
        '''Move goli up the screen'''
        self.y -= self.settings.goli_speed
        self.rect.y = self.y
        
    def draw_goli(self):
        '''Draw the bullet to the screen'''
        pygame.draw.rect(self.screen. self.color, self.rect)