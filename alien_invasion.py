import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from background import Background
from data import Data
from explosion import Explosion
from button import Button
from scoreboard import Scoreboard
def run_game():
    """initialize the game and create a screen object with settings"""
    pygame.init()
    ai_settings = Settings()  # create an instance of Settings and store it in ai_settings
    # create screen object and set the dimension
    # screen object section where an element is displayed is called a surface
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.screen_title)

    # use background image
    bg = Background(ai_settings, screen)
    # create a ship object
    ship = Ship(screen, ai_settings)

    # Create an alien object
    #alien = Alien(screen=screen, ai_settings=ai_settings)
    # create alien group
    aliens = Group()
    # make bullet instance of Group class
    # bullets = []
    bullets = Group()
    # create fleet of alien
    gf.create_alien_fleet(ai_settings, screen, aliens, ship)

    # create an instance of the game data class
    game_data = Data(ai_settings)

    # create explosion instance
    explosions = Group()

    # create button object to start the game
    msg = 'Start'
    play_button = Button(screen, ai_settings, game_data, msg)

    # Create scoreboard instance
    scoreboard = Scoreboard(screen, ai_settings, ship, aliens, bullets, game_data)

    # start the main loop for the game
    while True:
        # watch for keyboard and mouse event.
        gf.check_events(ship, ai_settings, bullets, screen, game_data, play_button, scoreboard)

        if game_data.is_game_active == True:
            """Check the status of is_game_active flag to determine when to end the game"""
            # move ship to the left/right as per the events
            Ship.move_ship(ship, ai_settings)
            # update bullet position and check for hitting an alien
            gf.update_bullet(bullets, ai_settings, aliens, screen, ship, explosions, game_data, scoreboard)
            gf.update_aliens(ship, ai_settings, aliens, bullets, game_data, screen, scoreboard)
        # update screen as per the events
        gf.update_screen(screen=screen, ship=ship, ai_settings=ai_settings, bullets=bullets, aliens=aliens, bg=bg,
                         play_button=play_button, game_data=game_data, scoreboard=scoreboard)

run_game()
