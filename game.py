import pygame
from random import randint
from sprites import Sara
from robot import Robot
from world import World
import sys


# TODO move this to a unique source
SCREEN_SIZE = (800, 600)


class Game:

    def __init__(self, screen):
        self.screen = screen

        SONG_END = pygame.USEREVENT + 1

#        pygame.mixer.pre_init(44100, -16, 2, 1024*4)

        pygame.mixer.music.load("intro.wav")
        pygame.mixer.music.set_endevent(SONG_END)
        pygame.mixer.music.play(1)


        clock = pygame.time.Clock()

        world = World()

        sara = Sara(world)
        sara.set_location(100, SCREEN_SIZE[1] / 2)
        world.add_entity(sara, ('events', 'player'))

        self.create_robot(world)
        self.create_robot(world)
        self.create_robot(world)

        should_quit = False
        while not should_quit:
            if randint(1, 500) == 1:
                self.create_robot(world)

            events = pygame.event.get()
            for event in events:
                if event.type == SONG_END:
                    pygame.mixer.music.load('main.wav')
                    pygame.mixer.music.play(-1)
            world.process_events(events)
            seconds_passed = clock.tick(60) / 1000.0
            should_quit = world.process(seconds_passed)
            world.render(screen)

            pygame.display.update()

        pygame.quit()
        sys.exit()

    def create_robot(self, world):
        robot = Robot(world)
        robot.set_location(randint(0, SCREEN_SIZE[0]), randint(0, SCREEN_SIZE[1]))
        world.add_entity(robot, ('enemies', ))
