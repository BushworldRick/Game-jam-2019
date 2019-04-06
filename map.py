import pygame
from Player import *
from config import *
from random import randint
from Enemy import *

max_stars = 200
stars = []
for i in range(max_stars):
    x,y = randint(0, 800), randint(0, 600)
    rad,spd = randint(2, 5), randint(100, 150)
    star = [x, y, rad, spd]
    stars.append(star)

NUM_ENEMIES = 20

class Map:
    def __init__(self):
        self.mStars = stars
        self.Player = Player((800,600), SHIP)
        self.mEnemies = []
        for i in range(NUM_ENEMIES):
            spwn_x = randint(0, win_width)
            self.mEnemies.append(Enemy(spwn_x, -50))
        self.Enemy_delay = 0.5
        self.Enemy_index = 1


    def update(self, dt):
        self.Enemy_delay -= dt
        if self.Enemy_delay < 0:
            self.Enemy_index += 1
            self.Enemy_delay = 0.5

        for star in self.mStars:
            star[1] += star[3] * dt
            if star[1] > star[2] + 600:
                star[1] = -star[2]

        self.Player.update(dt)

        for i in range(self.Enemy_index):
            self.mEnemies[i].update(dt)

    def input(self, evt):
        keys = pygame.key.get_pressed()
        self.Player.input(keys)

    def draw(self, win):
        for star in self.mStars:
            x = star[0]
            y = star[1]
            pygame.draw.circle(win, (220, 220, 220), (int(x), int(y)), star[2],)

        self.Player.draw(win)

        for i in range(self.Enemy_index):
            self.mEnemies[i].draw(win)
