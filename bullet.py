import pygame

from vector import Vector
from entity import Entity

# TODO: Create game_settings.py file
BLACK = (0, 0, 0)
LASER_IMG_FILENAME = "images/laser.png"
SCREEN_SIZE = (800, 600)

class Bullet(Entity):
    """ Make the bullets independant 
        Make the bullets great again """

    def __init__(self, player, world):

        # TODO: Player should not be an argument, instead, we could
        #       have a Weapon class. This will make the code easy to read,
        #       things like ammo and reload system could be implemented.
        sprite = pygame.image.load(LASER_IMG_FILENAME).convert()
        sprite.set_colorkey(BLACK)
        super(Bullet, self).__init__(world, 'bulllet', sprite)

        # Bullet settings
        self.speed = 300
        self.width = 5
        self.height = 15

        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.centerx = player.centerx
        self.rect.top = player.top

        # Store the bullet's position as a decimal value
        self.x = float(self.rect.x)

    def process(self, time_passed):
        if not self.destination:
            self.destination = Vector(SCREEN_SIZE[0] + self.image.get_width(),
                                      self.location.y)
        super(Bullet, self).process(time_passed)
