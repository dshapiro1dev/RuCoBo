import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initiate the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship impage and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ships location base on the movement flag"""
        if self.moving_right:
            if self.rect.x < (self.settings.screen_width - self.rect.width):
                self.rect.x += 1
        if self.moving_left:
            if self.rect.x > 0:
                self.rect.x -= 1

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)