import pygame.font


class Button:
    """Button class to add differnt buttons on game console"""
    def __init__(self, screen, ai_settings, game_data, msg):
        """Initialize the button attributes"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.game_data = game_data

        #  button properties
        self.button_width,  self.button_height = 200, 75
        self.button_color = (0, 250, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #  Create button rect and set it to the center of the screen
        self.rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.rect.center = self.screen_rect.center

        # prep the text
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """msg needs to be prepped"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_button(self):
        """draw button and then draw text_image on to of it"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
