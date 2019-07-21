
import pygame
class Background:
    """Background class to set the background image"""
    def __init__(self, ai_settings, screen):
        self.image_location = ai_settings.image_file_locations['background2']
        self.image = pygame.image.load(self.image_location)
        self.rect = self.image.get_rect()
        self.screen = screen

    def blitme(self):
        """blit the background"""
        self.screen.blit(self.image, self.rect)