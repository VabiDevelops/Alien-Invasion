import sys
import pygame

from settings import Settings
from player import Ship
from goli import Goli

class AlienInvasion:
    '''overall class to manage game assets and behavior'''
    def __init__(self):
        # initialize game, and create game resources
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.player = Ship(self)
        self.goli = pygame.sprite.Group()

    def run_game(self):
        # start the main loop for the game
        while True:
            self._check_events()
            self._update_screen()
            self.player.update()
            self.goli.update()
            
            self.clock.tick(60)
            
    def _check_events(self):
        '''respond to key and mouse presses'''
        for event in pygame.event.get():  
            #keydown movements
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)                
            #keyup movements   
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self,  event):
        '''response to keypresses'''
        if event.key == pygame.K_RIGHT:
            # Move ship to right
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move ship to left
            self.player.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_goli()
            
    def _check_keyup_events(self, event):
        '''response to key releases'''
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False
    
    def _fire_goli(self):
        '''Create a new bullet and add it to the bullets group'''
        new_goli = Goli(self)
        self.goli.add(new_goli)
    
    def _update_screen(self):
        '''updates images on the screen, and flip to the new screen'''
        self.screen.fill(self.settings.bg_color)
        for goli in self.goli.sprites():
            goli.draw_bullet()
        self.player.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance, run the game
    ai = AlienInvasion()
    ai.run_game()
