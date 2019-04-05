import pygame
from Player import *
from config import *
from random import randint

max_stars = 200
stars = []
for i in range(max_stars):
    x,y = randint(0, 800), randint(0, 600)
    rad,spd = randint(2, 5), randint(100, 150)
    star = [x, y, rad, spd]
    stars.append(star)

class Map:
    def __init__(self):
        self.mStars = stars
        self.Player = Player((800,600), SHIP)

    def update(self, dt):
        for star in self.mStars:
            star[1] += star[3] * dt
            if star[1] > star[2] + 600:
                star[1] = -star[2]
        self.Player.update(dt)

    def input(self, evt):
        keys = pygame.key.get_pressed()
        self.Player.input(keys)

    def draw(self, win):
        self.Player.draw(win)
        for star in self.mStars:
            x = star[0]
            y = star[1]
            pygame.draw.circle(win, (220, 220, 220), (int(x), int(y)), star[2],)
