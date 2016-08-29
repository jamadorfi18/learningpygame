from pygame.image import load as pygame_image_load
from vector import Vector
import pygame
from statemachine import StateMachine


BLACK = (0, 0, 0)
SARA_IMG_FILENAME = 'images/sara.png'
LASER_IMG_FILENAME = "images/laser.png"
SCREEN_SIZE = (800, 600)


class Entity(pygame.sprite.Sprite):

    def __init__(self, world, name, image):
        super(Entity, self).__init__()
        self.world = world
        self.name = name
        self.image = image
        self.rect = image.get_rect()
        self.location = Vector(0, 0)
        self.destination = None
        self.speed = 0.0

        self.brain = StateMachine()

        self.id = 0

    def set_location(self, x, y):
        self.location = Vector(x, y)
        self.rect.x = x
        self.rect.y = y

    def render(self, surface):
        x = self.location.x
        y = self.location.y
        surface.blit(self.image, (x, y))

    def process(self, time_passed):
        self.brain.think()
        if self.speed > 0 and self.location != self.destination:
            vec_to_destination = self.destination - self.location
            distance_to_destination = vec_to_destination.get_magnitude()
            vec_to_destination.normalize()
            travel_distance = min(distance_to_destination, time_passed * self.speed)
            vec_to_destination.x *= travel_distance
            vec_to_destination.y *= travel_distance
            self.set_location(self.location.x + vec_to_destination.x,
                              self.location.y + vec_to_destination.y)

    def keep_inside_screen(self):
        if self.destination.x < 0:
            self.destination.x = 0
        elif self.destination.x > SCREEN_SIZE[0] - self.image.get_width():
            self.destination.x = SCREEN_SIZE[0] - self.image.get_width()

        if self.destination.y < 0:
            self.destination.y = 0
        elif self.destination.y > SCREEN_SIZE[1] - self.image.get_height():
            self.destination.y = SCREEN_SIZE[1] - self.image.get_height()

class Sara(Entity):

    def __init__(self, world):
        sprite = pygame_image_load(SARA_IMG_FILENAME).convert_alpha()
        super(Sara, self).__init__(world, 'sara', sprite)
        self.speed = 200

    def process_events(self, events):
        pressed_keys = pygame.key.get_pressed()
        direction = Vector(0, 0)
        if pressed_keys[pygame.K_LEFT]:
            direction.x = -1
        elif pressed_keys[pygame.K_RIGHT]:
            direction.x = +1

        if pressed_keys[pygame.K_UP]:
            direction.y = -1
        elif pressed_keys[pygame.K_DOWN]:
            direction.y = +1
        direction.normalize()

        self.destination = self.location + Vector(
            direction.x * self.speed,
            direction.y * self.speed)

        self.keep_inside_screen()

        for event in events:
            if (event.type == pygame.KEYDOWN and
                event.key == pygame.K_SPACE):
                self.fire()

    def fire(self):
        # TODO if sara is moving and fires, laser appears in a previous locatiom
        x = self.location.x + 40
        y = self.location.y + 36
        shot = Shot(self.world)
        shot.set_location(x, y)
        self.world.add_entity(shot, ('ally_shots', ))


class Shot(Entity):
    def __init__(self, world):
        sprite = pygame_image_load(LASER_IMG_FILENAME).convert()
        sprite.set_colorkey(BLACK)
        super(Shot, self).__init__(world, 'shot', sprite)
        self.speed = 600

    def process(self, time_passed):
        if not self.destination:
            self.destination = Vector(
                SCREEN_SIZE[0] + self.image.get_width(),
                self.location.y
            )
        super(Shot, self).process(time_passed)
