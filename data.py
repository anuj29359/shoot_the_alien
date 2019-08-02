

class Data:
    """The class is to store game data"""

    def __init__(self, ai_settings):
        """initialize the game data"""
        self.ai_settings = ai_settings
        self.numberofships = 4
        self.reset_data()
        # start the game in inactive state
        self.is_game_active = False


    def reset_data(self):
        """reset the game data that can change during runtime"""
        self.ship_left = self.ai_settings.life_limit
