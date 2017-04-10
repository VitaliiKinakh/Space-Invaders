import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

def run_game():
    """Main game loop"""
    pygame.init()
    # Load settings
    ui_settings = Settings()
    # Create screen and set height and width
    screen = pygame.display.set_mode((ui_settings.width, ui_settings.height))
    #Set caption
    pygame.display.set_caption("Space Invaders")
    # Create ship
    ship = Ship(screen)
    # Create group of bullets
    bullets = Group()
    #Create aliens
    aliens = Group()
    gf.create_fleet(ui_settings, screen, ship, aliens)
    # Create stats
    stats = GameStats(ui_settings)
    #Create button for start game
    play_button = Button(ui_settings, screen)
    # Create score object
    score_board = ScoreBoard(ui_settings, screen, stats)
    # Main loop
    while True:
        # Catch events from keyboard and mouse
        gf.check_events(ui_settings, screen, stats,play_button, ship, bullets, aliens)
        if stats.game_active:
            # Move ship
            ship.update()
            # Update aliens
            gf.update_aliens(ui_settings, screen, aliens, ship, stats, bullets)
            # Move and remove bullets
            gf.update_bullets(ui_settings, screen,stats, score_board, ship, aliens, bullets)
        # Update screen during loop
        gf.update_screen(screen, ui_settings, ship, aliens, bullets,stats, play_button, score_board)
if __name__ == "__main__":
    run_game()
