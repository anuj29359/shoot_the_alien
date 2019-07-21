class Settings:
    """class settings will have different game settings"""
    def __init__(self ):
        """initialize the game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_upper_limit = -15
        self.bg_color = (230, 230, 230)  # light grey
        self.screen_title = 'Alien Invasion'
        # store the relative location of image files
        self.image_file_locations = {'ship': 'images\\ship.bmp',
                                     'hunter': 'images\\hunter_small.png',
                                     'hunter_xl': 'images\\hunter.png',
                                     'background1': 'images\\background.png',
                                     'background2': 'images/14wJuLo.png',
                                     'ship2': 'images\\ship2.png'
                                     }

        self.ship_image_location = self.image_file_locations['ship2']
        self.speed_factors = {'0.1x': 0.1,
                              '0.3x': 0.3,
                              '0.5x': 0.5,
                              '0.8x': 0.8,
                              '1x': 1,
                              '2x': 2,
                              '3x': 3,
                              '4x': 4,
                              '5x': 5,
                              '10x': 10,
                              '15x': 15,
                              '20x': 20,
                              '30x': 30,
                              '40x': 40,
                              '50x': 50}
        # speed of ship movement to left / right
        self.ship_speed = self.speed_factors['2x']
        self.step_size = self.ship_speed
        self.step_size_diagonal = self.ship_speed * 0.9

        # bullet settings
        self.bullet_width = 200
        self.bullet_height = 15
        self.bullet_width_large = 8  # for cannon
        self.bullet_speed = self.speed_factors['20x']
        self.bullet_color = 255, 150, 255

        # limit number of bullets
        self.bullet_limit = 4

        # Alien x-movement speed
        self.alien_speed = self.speed_factors['1x']

        # fleet drop speed
        self.fleet_drop_speed = self.speed_factors['5x']
        # Fleet direction = 1 for moving right and Fleet direction = -1 for moving left
        self.fleet_direction = 1

        # enable or disable printing logs
        self.print_logs = False
