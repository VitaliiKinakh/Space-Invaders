import pygame

class Ship():
    """Describes main character of game ship"""
    def __init__(self, screen):
        # Set screen
        self.screen = screen
        # Set image
        self.image = pygame.image.load("images/ship.png")
        # Get rect
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Set place for ship
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Frags for moving function
        self.moving_right = False
        self.moving_left = False


    def update(self):
        #Move ship
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 3
        elif self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 3

    def blitme(self):
        """Draw ship in current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center ship when ship colides with alien"""
        self.rect.centerx = self.screen_rect.centerx
