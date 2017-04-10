import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep



def check_keydown_events(event, ui_setting, screen, ship, bullets):
    """Check events when user push down button"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ui_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    """Check events when user ups button"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ui_setting, screen,stats,play_button, ship, bullets, aliens):
    """Checks all events during game"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Turns ship right or left
            check_keydown_events(event,ui_setting,screen,ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ui_setting,screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ui_settings, screen, stats, play_button,ship, aliens, bullets, mouse_x, mouse_y):
    """If mouse click button - start game"""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        #Settings
        ui_settings.initialize_dynamic_settings()
        # Reset stats
        stats.reset_stats()
        stats.game_active = True
        # Make bullets and aliens empty
        aliens.empty()
        bullets.empty()
        #Create new fleet and ship
        create_fleet(ui_settings, screen, screen, aliens)
        # Create new ship(center it)
        ship.center_ship()
        # Make mouse invisible
        pygame.mouse.set_visible(False)

def update_screen(screen, ui_setting, ship, aliens, bullets,stats, play_button, score_board):
    """Updates screen during game"""
    # Set color
    screen.fill(ui_setting.bg_color)
    #Draw bullets
    for bullet in bullets:
        bullet.draw_bullet()
    # Draw ship
    ship.blitme()
    # Draw alien
    aliens.draw(screen)
    # Show button
    # Show score
    score_board.show_score()
    if not stats.game_active:
        play_button.draw_button()
    #Show screen
    pygame.display.flip()

def update_bullets(ui_setting, screen,stats, sb, ship, aliens, bullets):
    """Updating bulets"""
    bullets.update()
    # Check for removing
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # Collision case - if bullet collides with alien - delete bullet and alien
        check_bullet_alien_collisions(ui_setting, screen, stats,sb,ship, aliens, bullets)
        # If all aliens are destroyed - create new fleet

def fire_bullet(ui_setting, screen, ship, bullets):
    # Create bullet and add to group
    if len(bullets) < ui_setting.bullets_n:
        newBullet = Bullet(ui_setting, screen, ship)
        bullets.add(newBullet)

def check_bullet_alien_collisions(ui_settings, screen, stats, sb, ship, aliens, bullets):
    """Bullet - alien collsion"""
    # Удаление пуль и пришельцев, участвующих в коллизиях.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stats.score += ui_settings.alien_points
        sb.prepare_score()
        check_high_score(stats, sb)

def create_fleet(ui_settings, screen,ship, aliens):
    """Creates alien fleet"""
    alien = Alien(ui_settings, screen)
    # Compute spare place for aliens
    alien_width = alien.rect.width
    number_aliens = get_number_alien(ui_settings, alien_width)
    #Create row of aliens
    for a_r in range(2):
        for a_n in range(number_aliens):
            create_alien(ui_settings, screen, aliens, a_n, a_r)

def get_number_alien(ui_settings, alien_width):
    """Computes number of aliens in row"""
    availiable_space = ui_settings.width - (alien_width + alien_width / 2)
    number_aliens = int(availiable_space / (alien_width + alien_width / 2)) - 1
    return number_aliens

def create_alien(ui_settings, screen, aliens, alien_number, row_number):
    """Creates objects - alien in group aliens"""
    alien = Alien(ui_settings, screen)
    # Set position of alien
    alien.x = alien.rect.width + (alien.rect.width + alien.rect.width / 2) * alien_number
    alien.rect.x = alien.x
    alien.rect.y = (alien.rect.height / 3) + (alien.rect.height * 1.5) * row_number
    # Add alien to group
    aliens.add(alien)


def update_aliens(ui_settings, screen, aliens, ship, stats, bullets):
    # We use update() for every alien
    aliens.update()
    # Check if fleet goes to edge
    check_fleet_edges(ui_settings, aliens)
    #If all aliens are destroyed
    if len(aliens) == 0:
        # bullets.empty()
        # Make game harder
        create_fleet(ui_settings, screen, ship, aliens)
        ui_settings.fleet_drop_speed += 1
        ui_settings.alien_points += 5
        ui_settings.alien_speed += 1
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ui_settings,stats, screen, ship, aliens, bullets)
    # Check aliens bottom
    check_aliens_bottom(ui_settings, screen, stats, ship, aliens, bullets)

def check_fleet_edges(ui_settings, aliens):
    """Check if any of fleet go to eadge"""
    # Then change fleet direction
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ui_settings, aliens)
            break

def change_fleet_direction(ui_settings, aliens):
    """Change direction and move fleet down"""
    for alien in aliens.sprites():
        alien.rect.y += ui_settings.fleet_drop_speed
    ui_settings.direction *= -1

def ship_hit(ui_settings, stats, screen, ship, aliens, bullets):
    """Ship - alien hit"""
    # Decrease lives
    if stats.ships_left > 0:
        stats.ships_left -= 1
        #  Clear aliens and bullets
        aliens.empty()
        bullets.empty()
        # Create new fleet
        create_fleet(ui_settings, screen, ship, aliens)
        ship.center_ship()
        # Wait for 0.5 sec
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        stats.reset_stats()

def check_aliens_bottom(ui_settings, screen, stats, ship, aliens, bullets):
    """Check if aliens are near bottom"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # The same thing when ship - alien collision
            ship_hit(ui_settings,stats,screen,ship,aliens,bullets)
            break

def check_high_score(stats, score_board):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score_board.prepare_high_score()