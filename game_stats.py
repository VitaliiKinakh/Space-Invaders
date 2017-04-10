class GameStats():
    """Class for game statistic"""
    def __init__(self, ui_settings):
        self.ui_settings = ui_settings
        self.game_active = False
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        """Reset stats for gsme"""
        self.ships_left = self.ui_settings.ships_num
        self.score = 0