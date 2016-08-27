from pygame.image import load as pygame_image_load


BLACK = (0, 0, 0)
SARA_IMG_FILENAME = 'images/sara.png'
LASER_IMG_FILENAME = "images/laser.png"
SCREEN_SIZE = (640, 480)
ROBOT_IMAGE_FILENAME = "images/robot.png"


class Sprite(object):
    def __init__(self, x, y, sprite=None):
        self.x = x
        self.y = y
        self.sprite = sprite

    def blit(self, screen):
        screen.blit(self.sprite, self.get_pos())

    def get_pos(self):
        return (self.x, self.y)

class Sara(Sprite):

    SPEED = 300

    def __init__(self, x, y):
        sprite = pygame_image_load(SARA_IMG_FILENAME).convert_alpha()
        super(Sara, self).__init__(x, y, sprite)

    def move(self, seconds_passed, move_x, move_y):
        self.x += Sara.SPEED * move_x * seconds_passed
        self.y += Sara.SPEED * move_y * seconds_passed

        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_SIZE[0] - self.sprite.get_width():
            self.x = SCREEN_SIZE[0] - self.sprite.get_width()

        if self.y < 0:
            self.y = 0
        elif self.y > SCREEN_SIZE[1] - self.sprite.get_height():
            self.y = SCREEN_SIZE[1] - self.sprite.get_height()


class Shot(Sprite):
    NUMBER_SHOTS = 0
    SPEED = 600

    def __init__(self, x, y):
        sprite = pygame_image_load(LASER_IMG_FILENAME).convert()
        sprite.set_colorkey(BLACK)
        super(Shot, self).__init__(x, y, sprite)

    def move(self, seconds_passed):
        self.x += seconds_passed * Shot.SPEED
        if self.x > SCREEN_SIZE[0]:
            return False
        return True

    @staticmethod
    def fire(x, y): # static
        Shot.NUMBER_SHOTS += 1
        return Shot(x, y)

class Robot(Sprite):

    def __init__(self, x, y):
        sprite = pygame_image_load(ROBOT_IMAGE_FILENAME).convert_alpha()
        super(Robot, self).__init__(x, y, sprite)

LASER_IMAGE_FILENAME = 'images/redlaser.png'
class Laser(Sprite):

    def __init__(self, x, y):
        sprite = pygame_image_load(LASER_IMAGE_FILENAME).convert_alpha()
        super(Laser, self).__init__(x, y, sprite)

    def move(self, seconds_passed):
        self.x -= seconds_passed * 10 #Shot.SPEED
        if self.x < 0:
            return False
        return True
