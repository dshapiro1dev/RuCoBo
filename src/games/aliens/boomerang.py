import pygame
import os
from pygame.sprite import Sprite

class Boomerang(Sprite):
    """A class to manage the super space boomerang!"""

    def __init__(self, ai_game):
        """Create the boomerang"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the boomerang image and get its rect.
        self.image = pygame.image.load(os.getcwd() + "/images/Boomerang.png")
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop
        self.rect.y -= 60
        self.x = float(self.rect.x)

        # Store the boomerang's position as a decimal value
        self.y = float(self.rect.y)
        self.speed_factor = self.settings.boomerang_speed
        self.x_speed_factor = self.settings.boomerang_x_speed

        # Set the direction of the boomerang
        self.boomerang_forward = True

        # Get a reference to the ship so that the boomerang can move towards it
        self.ship = ai_game.ship

    def update(self):
        """Logic for moving the boomerang"""
        if self.y < 0:
            self.boomerang_forward = False

        # Update the decimal y position of the boomerang
        if self.boomerang_forward:
            self.y -= self.speed_factor
        else:
            self.y += self.speed_factor
        # update the rect position
        self.rect.y = self.y

        # Make the boomerang head back towards the ship
        ship_pos = self.ship.x
        if not self.boomerang_forward:
            if self.x < ship_pos:
                self.x += self.x_speed_factor
            elif self.x > ship_pos:
                self.x -= self.x_speed_factor

        self.rect.x = self.x

    def blitme(self):
        """draw the boomerang at its current location"""
        self.screen.blit(self.image, self.rect)