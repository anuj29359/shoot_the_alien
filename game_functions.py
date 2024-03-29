import pygame
import sys
from bullet import Bullet
from alien import Alien

def fire_bullet(bullets,ai_settings,ship, screen):
    if len(bullets) < ai_settings.bullet_limit:
        new_bullet = Bullet(ship, screen, ai_settings)
        new_bullet.shoot_sound.play()
        # bullets.append(new_bullet)
        bullets.add(new_bullet)
        if ai_settings.print_logs:
            print('added new bullet to bullets, total bullets on the screen: ' + str(len(bullets)))
            print('Speed of bullet is : ' + str(new_bullet.bullet_speed))

def check_keydown_event(event, ship, screen, ai_settings, bullets):
    """check which key has been pressed and then act accordingly to move the ship or fire bullet"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True

    if event.key == pygame.K_SPACE:
        fire_bullet(bullets, ai_settings, ship, screen)


def check_keyup_event(event, ship):
    """check which key has been released and then act accordingly to stop the ship or fire bullet"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ship, ai_settings, bullets, screen):
    """check the keyboard or mouse input and respond"""
    for event in pygame.event.get():
        # Exit the game screen when clicked on the cross button
        if event.type == pygame.QUIT:
            if ai_settings.print_logs:
                print('Closed the game window ny clicking on the cross button')
            sys.exit()
        # set the flag to move ship to the right or left
        elif event.type == pygame.KEYDOWN:
            if ai_settings.print_logs:
                print('pressed the key: {0}'.format(event.key))
            check_keydown_event(event=event, ship=ship, ai_settings=ai_settings, bullets=bullets, screen=screen)
        # reset the moving left/right flag after the arrow key has been released
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def update_screen(screen, ship, ai_settings, bullets , aliens, bg):
    """update the screen based on the events and settings"""
    # set the background color of the screen
    bg.blitme()
    #screen.fill(ai_settings.bg_color)

    # add ship to the game screen
    ship.blitme()
    aliens.draw(screen)

    # redraw all bullets behind ship
    # for bullet in bullets:
    #    bullet.draw_bullet()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # make the most recently drawn screen displayed
    pygame.display.flip()


def update_bullet(bullets, ai_settings, aliens, screen, ship):
    """move the bullets upward and kill it after it has crossed the top og the screen"""
    for bullet in bullets.sprites():
        bullet.update()

    # kill the bullet which has crossed the screen
    for bullet in bullets:
        # print('bullet ret y = ' + str(bullet.rect.y))
        if bullet.rect.y < ai_settings.screen_upper_limit:
            bullets.remove(bullet)
    # checks the collision between a bullet and a alien an remove the bullet/alien from their Sprite Group
    collision = check_collision_alien_bullet(bullets, aliens)
    # Create a new fleet after all the aliens have been destroyed
    create_new_fleet(aliens, bullets, ai_settings, screen, ship)


def check_collision_alien_bullet(bullets, aliens):
    """checks the collision between a bullet and a alien an remove the bullet/alien from their Sprite Group"""
    return pygame.sprite.groupcollide(bullets, aliens, True, True)

def get_number_aliens_x(ai_settings, alien_width):
    """find the number of aliens in one row"""
    alien_cnt_per_row = (ai_settings.screen_width - 2 * alien_width) // (2 * alien_width)
    return alien_cnt_per_row

def get_number_rows(ai_settings, alien_height, ship_height):
    alien_rows_cnt = (ai_settings.screen_height - 15 * alien_height - ship_height) // (2 * alien_height)
    return alien_rows_cnt

def create_alien(ai_settings, screen, aliens, alien_number, alien_row_num):
    """create an alien object"""
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width * 2 * alien_number + alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien_height + alien_height * 2 * alien_row_num
    aliens.add(alien)


def create_alien_fleet(ai_settings, screen, aliens, ship):
    """Create a fleet of aliens"""
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    alien_cnt_per_row = get_number_aliens_x(ai_settings, alien_width)
    alien_rows_cnt = get_number_rows(ai_settings, alien_height, ship_height)

    for alien_row_num in range(alien_rows_cnt):
        for alien_number in range(alien_cnt_per_row):
            create_alien(ai_settings,screen, aliens, alien_number, alien_row_num)
            #print('There are {0} aliens on the screen.'.format(aliens))
            #if len(aliens) < (alien_cnt_per_row * alien_number_of_rows):
            #    alien = Alien(screen, ai_settings)
            #    alien.rect.x = 2 * alien_width * (row + 1)
            #    alien.rect.y = alien_height * (col + 1)
            #    aliens.add(alien)


def check_fleet_edge(ai_settings, aliens):
    """check if any alien in the fleet has hit the edge"""
    for alien in aliens.sprites():
        if(alien.check_edge()):
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """drop the fleet and change the direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens):
    check_fleet_edge(ai_settings, aliens)
    aliens.update()


def create_new_fleet(aliens, bullets, ai_settings, screen, ship):
    """Create new fleet after all the aliens have been destroyed"""
    if len(aliens) == 0:
        bullets.empty()
        create_alien_fleet(ai_settings, screen, aliens, ship)




