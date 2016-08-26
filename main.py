#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'grass.png'
cursor_image_filename = 'gauntlet.png'
SARA_IMG_FILENAME = 'sara.png'
LASER_IMG_FILENAME = "laser.png"
SCREEN_SIZE = (640, 480)

BLACK = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, 0 , 32)
pygame.display.set_caption("Push goblins")

background = pygame.image.load(background_image_filename).convert()
cursor = pygame.image.load(cursor_image_filename).convert_alpha()
sara = pygame.image.load(SARA_IMG_FILENAME).convert_alpha()
laser = pygame.image.load(LASER_IMG_FILENAME).convert()
laser.set_colorkey(BLACK)

move_x = 0
move_y = 0
sara_x = SCREEN_SIZE[0] / 2
sara_y = SCREEN_SIZE[1] / 2
shots = []

class Shot():
    SPEED = 2
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = laser

    def move(self):
        self.x += Shot.SPEED

    def get_pos(self):
        return (self.x, self.y)

    def blit(self, screen):
        screen.blit(self.sprite, self.get_pos())

def fire(x, y):
    shots.append(Shot(x, y))
    return True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = +1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = +1
            elif event.key == 32:  # spacebar for shot
                fire(sara_x + sara.get_width(), sara_y + 36)
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0
            elif event.key == K_RIGHT:
                move_x = 0
            elif event.key == K_UP:
                move_y = 0
            elif event.key == K_DOWN:
                move_y = 0
    sara_x += move_x
    sara_y += move_y

    if sara_x < 0:
        sara_x = 0
    elif sara_x > SCREEN_SIZE[0] - sara.get_width():
        sara_x = SCREEN_SIZE[0] - sara.get_width()

    if sara_y < 0:
        sara_y = 0
    elif sara_y > SCREEN_SIZE[1] - sara.get_height() :
        sara_y = SCREEN_SIZE[1] - sara.get_height()

    screen.blit(background, (0, 0))
    screen.blit(sara, (sara_x, sara_y))

    for shot in shots:
        shot.move()
        shot.blit(screen)

    x, y = pygame.mouse.get_pos()
    x -= cursor.get_width() / 2
    y -= cursor.get_height() / 2
    screen.blit(cursor, (x, y))

    pygame.display.update()
