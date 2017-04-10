from pygame.sprite import  Sprite
import pygame

class Bullet(Sprite):

    def __init__(self, ui_settings, screen, ship):
        """Class for bullets"""
        super().__init__()
        self.screen = screen
        # Create bullet at position (0, 0)
        self.rect = pygame.Rect(0, 0, ui_settings.bullet_width, ui_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.centerx
        self.y = self.rect.y
        # Set color
        self.color = ui_settings.bullet_color
        # Set speed
        self.speed = ui_settings.bullet_speed

    def update(self):
        """Change position of bullet"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet"""
        pygame.draw.rect(self.screen,self.color,self.rect)

