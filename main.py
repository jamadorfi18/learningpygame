#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit

# Useful constants
SCREEN_SIZE = (640, 480)
BLACK = (0, 0, 0)

# Images
BACKGROUND_IMG_FILENAME = 'images/grass.png'
CURSOR_IMG_FILENAME = 'images/gauntlet.png'
SARA_IMG_FILENAME = 'images/sara.png'
LASER_IMG_FILENAME = "images/laser.png"

# init
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode(SCREEN_SIZE, 0 , 32)
pygame.display.set_caption("Push goblins")

background = pygame.image.load(BACKGROUND_IMG_FILENAME).convert()
cursor = pygame.image.load(CURSOR_IMG_FILENAME).convert_alpha()
laser = pygame.image.load(LASER_IMG_FILENAME).convert()
laser.set_colorkey(BLACK)
font = pygame.font.SysFont('lobster', 16)
number_shots = 0
text_surface = font.render('Sara has made {} shots'.format(number_shots), True, BLACK)

class Sprite():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sprite = None
        
    def blit(self):
        screen.blit(self.sprite, self.get_pos())
        
    def get_pos(self):
        return (self.x, self.y)

class Sara(Sprite):

    SPEED = 300

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(SARA_IMG_FILENAME).convert_alpha()

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
        self.x = x
        self.y = y
        self.sprite = laser

    def move(self, seconds_passed):
        self.x += seconds_passed * Shot.SPEED
        if self.x > SCREEN_SIZE[0]:
            return False
        return True

    @staticmethod
    def fire(x, y): # static
        Shot.NUMBER_SHOTS += 1
        shots.append(Shot(x, y))

# Sprites
sara = Sara(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2)
shots = []
move_x = 0
move_y = 0

# main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = 1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
            elif event.key == 32:  # spacebar for shot
                sara_pos = sara.get_pos()
                Shot.fire(sara_pos[0] + sara.sprite.get_width(), sara_pos[1] + 36)
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0
            elif event.key == K_RIGHT:
                move_x = 0
            elif event.key == K_UP:
                move_y = 0
            elif event.key == K_DOWN:
                move_y = 0

    seconds_passed = clock.tick(60) / 1000.0  # 60 frames per second, pc mustard race
    sara.move(seconds_passed, move_x, move_y)

    screen.blit(background, (0, 0))
    sara.blit()

    cursor_x, cursor_y = pygame.mouse.get_pos()
    cursor_x -= cursor.get_width() / 2
    cursor_y -= cursor.get_height() / 2
    screen.blit(cursor, (cursor_x, cursor_y))
    
    text_surface = font.render('Sara has made {} shots'.format(Shot.NUMBER_SHOTS), True, BLACK)
    screen.blit(text_surface, (20, 20))

    for shot in shots:
        is_still_in = shot.move(seconds_passed)
        shot.blit()
        if not is_still_in:
            del shots[shots.index(shot)]

    pygame.display.update()
