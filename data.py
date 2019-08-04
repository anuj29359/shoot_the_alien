import pygame

class Data:
    """The class is to store game data"""

    def __init__(self, ai_settings):
        """initialize the game data"""
        self.ai_settings = ai_settings
        self.ship_left = self.ai_settings.life_limit
        self.reset_data()
        # start the game in inactive state
        self.is_game_active = False


    def reset_data(self):
        """reset the game data that can change during runtime"""
        self.ship_left = self.ai_settings.life_limit

    def set_game_inactive(self):
        """set the flag is_game_active = False and hide the cursor"""
        self.is_game_active = False
        # show the mouse cursor
        pygame.mouse.set_visible(True)

    def set_game_active(self):
        """set the flag is_game_active = False and hide the cursor"""
        self.is_game_active = True
        # show the mouse cursor
        pygame.mouse.set_visible(False)