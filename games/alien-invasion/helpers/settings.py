class Settings():
    """A class to store all settings for alien invasion"""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_w = 1200
        self.screen_h = 800
        self.bg_color = (230, 230, 230)
        # Ship settings
        self.ship_speed_factor = 1.5 
        # Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.screen_bullet_limit = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # where 1 is right and -1 is left
