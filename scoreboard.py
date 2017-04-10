import pygame.font

class ScoreBoard():
    """Class for score: max and current"""
    def __init__(self, ui_settings, screen, stats):
        # Set screen for record message
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ui_settings = ui_settings
        self.stats = stats
        # Settings for message
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Prepare score
        self.prepare_score()
        self.prepare_high_score()

    def prepare_score(self):
        # Make a string
        score_str = str(self.stats.score)
        # Make a image
        self.score_image = self.font.render(score_str, True, self.text_color, self.ui_settings.bg_color)
        # Get rect for image and set image
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prepare_high_score(self):
        """Prepare high score to visualize"""
        high_score = str(self.stats.high_score)
        # Make a image
        self.high_score_image = self.font.render(high_score, True, self.text_color, self.ui_settings.bg_color)
        # Get rect for image and set iamge
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top


    def show_score(self):
        """Shows score"""
        self.screen.blit(self.score_image, self.screen_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)



