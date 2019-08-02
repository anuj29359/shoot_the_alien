import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Alien class inherited from Sprite"""

    def __init__(self, screen, ai_settings):
        """initialize an alien object"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images\\alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.n = 0

    def blitme(self):
        """draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        """check if the fleet hit the edge of the screen"""
        self.screen_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True
        else:
            return False



    def update(self):
        """move the alien to the left or right"""
        self.n += 1
        if self.ai_settings.print_logs:
            print(str(self.n) + '. - 0 value of self.x is : ' + str(self.x) + ' rect.x is ' + str(self.rect.x))
        self.x = self.rect.x
        self.x += self.ai_settings.alien_speed * self.ai_settings.fleet_direction
        if self.ai_settings.print_logs:
            print(str(self.n) + '. - 1 value of self.x is : ' + str(self.x) + ' rect.x is ' + str(self.rect.x))
        self.rect.x = self.x

        if self.ai_settings.print_logs:
            print(str(self.n) + '. - 2 value of self.x is : ' + str(self.x) + ' rect.x is ' + str(self.rect.x))
            print('Alien_Speed is : ' + str(self.ai_settings.alien_speed))


