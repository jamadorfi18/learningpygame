import sys

from pygame.image import load as pygame_image_load
from sprites import Entity


WALL_IMG_FILENAME = 'images/wall.png'


class Wall(Entity):

    def __init__(self, world):
        sprite = pygame_image_load(WALL_IMG_FILENAME).convert_alpha()
        super(Wall, self).__init__(world, 'wall', sprite)
