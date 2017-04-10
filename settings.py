class Settings():
    """Class for setting for game window"""
    def __init__(self):
        # Settings for game arena
        self.width = 1200
        self.height = 640
        self.bg_color= (255, 255, 255)
        # Settings for bullets
        self.bullet_speed = 3
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # Set number of bullets alowed
        self.bullets_n = 3
        #Set speed of alien
        # Set directions
        self.dir = 1 # 1 move right -1 move left
        # Speed down
        self.fleet_drop_speed = 10
        # Number of ships for game
        self.ships_num = 3
        self.points = 25
        self.a_s = 1
        self.f_d_s = 10


    def initialize_dynamic_settings(self):
        """Initialize settings for new game"""
        # Set speed of alien
        self.alien_speed = self.a_s
        # Set directions
        self.direction = self.dir # 1 move right -1 move left
        # Speed down
        self.fleet_drop_speed = self.f_d_s
        # Points for every alien
        self.alien_points = self.points
