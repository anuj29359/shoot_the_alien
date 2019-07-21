import pygame

class Ship:
    """Ship class to dfine diffrent properties of the spaceship"""
    def __init__(self, screen, ai_settings):
        """initialise the ship display on the screen"""

        self.screen = screen
        # get the screen rectangle dimension
        self.screen_rect = screen.get_rect()
        # load ship image file location in a variable

        image_file_location = ai_settings.ship_image_location
        try:
            # get the ship image
            self.image = pygame.image.load(image_file_location)
            # get ship image rectangle dimension
            self.rect = self.image.get_rect()

            # position the ship at center-bottom of the screen
            self.rect.bottom = self.screen_rect.bottom
            self.rect.centerx = self.screen_rect.centerx
            self.ship_x = float(self.rect.centerx)
            self.ship_y = float(self.rect.bottom)
        except FileNotFoundError or FileExistsError:
            print('File : "{0}", not found'.format(image_file_location))

        # flags for continuous movement of the ship
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def move_circular(self, ai_settings):

        # move right up
        if self.moving_right is True and self.moving_up is True:
            if self.rect.bottom >= ai_settings.screen_height // 2:
                self.ship_y -= ai_settings.step_size_diagonal
                self.rect.bottom = self.ship_y
            if self.rect.centerx < ai_settings.screen_width:
                self.ship_x += ai_settings.step_size_diagonal
                self.rect.centerx = self.ship_x
            else:
                self.ship_x = self.rect.centerx = 0

        # move right downward
        if self.moving_right is True and self.moving_down is True:
            if self.rect.bottom <= ai_settings.screen_height:
                self.ship_y += ai_settings.step_size_diagonal
                self.rect.bottom = self.ship_y
            if self.rect.centerx < ai_settings.screen_width:
                self.ship_x+= ai_settings.step_size_diagonal
                self.rect.centerx = self.ship_x
            else:
                self.ship_x = self.rect.centerx = 0

        # move left upward
        if self.moving_left is True and self.moving_up is True:
            if self.rect.bottom >= ai_settings.screen_height // 2:
                self.ship_y -= ai_settings.step_size_diagonal
                self.rect.bottom = self.ship_y
            if self.rect.centerx >= 0:
                self.ship_x -= ai_settings.step_size_diagonal
                self.rect.centerx = self.ship_x
            else:
                self.ship_x = self.rect.centerx = ai_settings.screen_width

        # move left downward
        if self.moving_left is True and self.moving_down is True:
            if self.rect.bottom <= ai_settings.screen_height:
                self.ship_y += ai_settings.step_size_diagonal
                self.rect.bottom = self.ship_y
            if self.rect.centerx >= 0:
                self.ship_x -= ai_settings.step_size_diagonal
                self.rect.centerx = self.ship_x
            else:
                self.ship_x = self.rect.centerx = ai_settings.screen_width


    def move_ship(self, ai_settings):
        """move the ship depending on the flag to move either right or left"""

        self.move_circular(ai_settings)

        if self.moving_right:
            if self.rect.centerx < ai_settings.screen_width:

                # move the ship to the right
                self.ship_x += ai_settings.step_size
                self.rect.centerx = self.ship_x
                if ai_settings.print_logs:
                    print(self.ship_x)
                    print("moving the ship to the right")
                    print('ship_location : x = ' + str(self.rect.centerx))
            else:
                self.ship_x = self.rect.centerx = 0
                if ai_settings.print_logs:
                    print("Its the extreme right, ship takes circular turn and comes out from left side of the screen.")
        elif self.moving_left:
            if self.rect.centerx >= 0:
                # move the ship to the right
                self.ship_x -= ai_settings.step_size
                self.rect.centerx = self.ship_x

                if ai_settings.print_logs:
                    print("moving the ship to the left")
                    print('ship_location : x = ' + str(self.rect.centerx))
            else:
                self.ship_x = self.rect.centerx = ai_settings.screen_width
                if ai_settings.print_logs:
                    print("Its the extreme left, ship takes circular turn and comes out from right side of the screen.")
        elif self.moving_up:
            if self.rect.bottom >= ai_settings.screen_height//2:
                # move the ship upward
                self.ship_y -= ai_settings.step_size
                self.rect.bottom = self.ship_y
                if ai_settings.print_logs:
                    print("moving the ship upward")
                    print('ship_location : y = ' + str(self.rect.bottom))
            else:
                if ai_settings.print_logs:
                    print("Its the extreme top the ship can be elevated.")
        elif self.moving_down:
            if self.rect.bottom < ai_settings.screen_height:
                # move the ship to the right
                self.ship_y += ai_settings.step_size
                self.rect.bottom = self.ship_y
                if ai_settings.print_logs:
                    print("moving the ship downward")
                    print('ship_location : y = ' + str(self.rect.bottom))
            else:
                if ai_settings.print_logs:
                    print("Its the bottom most surface the ship can go.")

    def blitme(self):
        """drew the ship at its current location"""
        # blit(Surface, size)
        self.screen.blit(self.image, self.rect)


