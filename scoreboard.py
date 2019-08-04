import pygame.font
from pygame.sprite import Group
import json
from ship import Ship

class Scoreboard:
    """manage the data of number of alients hit by the ship"""
    def __init__(self, screen, ai_settings, ship, aliens, bullets, game_data):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.ship = ship
        self.aliens = aliens
        self.bullets = bullets
        self.game_data = game_data
        self.highest_score = self.get_highest_score()

        #  font setting for scoring information
        self.font = pygame.font.SysFont(None, 22)
        self.text_color = 255, 255, 255

        # prep the scoreboard - remaining ships, highest score and score
        self.prep_remaining_ships()
        self.prep_score()
        self.prep_highest_score()

        # remaining life - the ships

    def prep_remaining_ships(self):
        """prep the remaining ships on the scoreboard"""
        self.ships = Group()
        for ship_num in range(self.game_data.ship_left - 1):
            ship = Ship(self.screen, self.ai_settings)
            ship.rect.top = 10
            ship.rect.right = 80 + ship.rect.width * ship_num
            self.ships.add(ship)


    def prep_score(self):
        """convert the score text into an image"""
        if self.game_data.score < self.highest_score:
            self.text_color = 255, 255, 255
        self.score_image = self.font.render('Score: ' + str(self.game_data.score), False, self.text_color)
        # display the score on the top right of the screen
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 15
        self.score_image_rect.top = self.screen_rect.top + 15

    def prep_highest_score(self):
        """convert the highest_score text into an image"""
        self.highest_score_image = self.font.render('Highest Score: ' + str(self.highest_score), False, self.text_color)
        # display the score at the top center of the screen
        self.highest_score_image_rect = self.highest_score_image.get_rect()
        self.highest_score_image_rect.centerx = self.screen_rect.centerx
        self.highest_score_image_rect.top = self.screen_rect.top + 15

    def show_score(self):
        """display the score on the screen"""
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_image_rect)
        self.ships.draw(self.screen)

    def get_highest_score(self):
        """read highest score from the data.json file"""
        with open(self.ai_settings.data_file_location, 'r') as data_file:
            return json.load(data_file)

    def set_highest_score(self):
        """if current score is more than the highest score the update the highest score"""
        if self.game_data.score > self.highest_score:
            self.text_color = 255, 0, 0
            self.highest_score = self.game_data.score
            with open(self.ai_settings.data_file_location, 'w') as data_file:
                json.dump(self.highest_score, data_file)
