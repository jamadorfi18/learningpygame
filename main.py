#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit
from sprites import Sara, Shot, Robot, Laser

# Useful constants
SCREEN_SIZE = (640, 480)
BLACK = (0, 0, 0)

# Images
BACKGROUND_IMG_FILENAME = 'images/grass.png'
CURSOR_IMG_FILENAME = 'images/gauntlet.png'

# init
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode(SCREEN_SIZE, 0 , 32)
pygame.display.set_caption("Push goblins")

background = pygame.image.load(BACKGROUND_IMG_FILENAME).convert()
cursor = pygame.image.load(CURSOR_IMG_FILENAME).convert_alpha()
font = pygame.font.SysFont('lobster', 16)
number_shots = 0
text_surface = font.render('Sara has made {} shots'.format(number_shots), True, BLACK)


# Sprites
sara = Sara(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2)
shots = []
move_x = 0
move_y = 0
robot = Robot(600, 400)
robot_laser = Laser(20, 8)
rl_w = robot_laser.sprite.get_width()
rl_h = robot_laser.sprite.get_height()
robot_laser.x = robot.x + 20 - rl_w
robot_laser.y = robot.y + 8 - rl_h / 2
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
                shots.append(Shot.fire(sara_pos[0] + sara.sprite.get_width(), sara_pos[1] + 36))
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
    sara.blit(screen)
    robot.blit(screen)
    robot_laser.blit(screen)
    robot_laser.move(seconds_passed)

    cursor_x, cursor_y = pygame.mouse.get_pos()
    cursor_x -= cursor.get_width() / 2
    cursor_y -= cursor.get_height() / 2
    screen.blit(cursor, (cursor_x, cursor_y))
    
    text_surface = font.render('Sara has made {} shots'.format(Shot.NUMBER_SHOTS), True, BLACK)
    screen.blit(text_surface, (20, 20))

    for shot in shots:
        is_still_in = shot.move(seconds_passed)
        shot.blit(screen)
        if not is_still_in:
            del shots[shots.index(shot)]

    pygame.display.update()
