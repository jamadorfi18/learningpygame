import pygame
import menu
from random import randint
from sara import Sara
from robot import Robot
from world import World


SCREEN_SIZE = (800, 600)

def main():
    pygame.init()
    pygame.mouse.set_visible(0)
    pygame.display.set_caption('Sara\'s shooter')
    screen = pygame.display.set_mode(SCREEN_SIZE)
    menu.MainMenu(screen)

if __name__ == '__main__':
    main()
