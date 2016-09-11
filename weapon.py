import pygame

from bullet import Bullet

class Weapon():

    def __init__(self, player, world):
        self.magazine = []
        self.magazine_size = 10
        self.bullets_remaining = 0
        self.reloading = False

        self.player = player
        self.world = world
        self.reload()

    def reload(self):
        self.reloading = True
        for i in xrange(self.magazine_size - self.bullets_remaining):
            bullet = Bullet(self.world)
            self.magazine.append(bullet)

        self.bullets_remaining = self.magazine_size
        self.reloading = False

    def fire(self):
        x = self.player.location.x + self.player.width
        y = self.player.location.y + self.player.height / 2

        if self.bullets_remaining > 0:
            bullet = self.magazine.pop()
            bullet.set_location(x, y)
            self.bullets_remaining -= 1
            self.world.add_entity(bullet, ('ally_shots', ))
        else:
            print 'no ammo'
