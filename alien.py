from pygame.sprite import Sprite
import pygame

class Alien(Sprite):
    """Describes alien"""
    def __init__(self, ui_settings, screen):
        #Set basic qualities
        super().__init__()
        self.screen = screen
        self.ui_settings = ui_settings
        # Load image
        self.image = pygame.image.load("images/alien.png")
        self.rect = self.image.get_rect()
        # Set default position
        self.rect.x = self.rect.width / 2
        self.rect.y = 0
        # Save position
        self.x = self.rect.x

    def blitme(self):
        """Blit image"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move alien"""
        self.x += self.ui_settings.alien_speed * self.ui_settings.direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is near edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= 1200:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False

