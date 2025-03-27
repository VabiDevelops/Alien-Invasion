class Settings:
    '''A class to store all settings for Alien Invasion'''

    def __init__(self):
        ''' initialize the game's settings '''
        # screen settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship's speed
        self.ship_speed = 5
        
        # goli settings
        self.goli_speed = 2.5
        self.goli_width = 3
        self.goli_height = 15
        self.goli_color = (60, 60, 60)
        