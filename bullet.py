import pygame
from pygame.sprite import Sprite


# I have deliberately not used Sprite-Groups pygame classes for Bullet
# To use it , uncomment the comments starting with #1 and replace the conventional instructions

class Bullet(Sprite): #1 Bullet(Sprite)
    """bullet class: manage the bullets fired from a ship"""
    def __init__(self, ship, screen, ai_settings):
        """create bullet object at the current position of the ship"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # position the bullet at the top of the ship
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # converting the y dimension into float type
        self.y = float(self.rect.y)

        # load game sound
        # bullet fire sound
        self.shoot_sound = pygame.mixer.Sound('sound\\Laser_Shoot2.wav')

        # set the bullet speed and color as defined in the settings file
        self.bullet_speed = ai_settings.bullet_speed
        self.bullet_color = ai_settings.bullet_color



    def update(self):
        """move the bullet upward (away from the ship)"""
        # update the float position of the bullet

        self.y -= self.bullet_speed
        # update the rect value of the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on the screen as per the color and rect size define"""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)
