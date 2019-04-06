import pygame
from Player import *
from config import *
from random import randint
from Enemy import *
from bullet import *

NUM_ENEMIES = 20

class Map:
    def __init__(self):
        self.Player = Player((800,600), SHIP)
        self.mEnemies = []
        for i in range(NUM_ENEMIES):
            spwn_x = randint(0, win_width)
            self.mEnemies.append(Enemy(spwn_x, -50))
        self.Enemy_delay = 0.5
        self.Enemy_index = 1
        self.bullet_list = []


    def update(self, dt):

        if self.Enemy_index < NUM_ENEMIES:
            self.Enemy_delay -= dt
            if self.Enemy_delay < 0:
                self.Enemy_index += 1
                self.Enemy_delay = 0.5

        self.Player.update(dt)

        for i in range(self.Enemy_index):
            self.mEnemies[i].update(dt)

    def input(self, evt, keys):
        self.Player.input(keys)


    def draw(self, win):

        self.Player.draw(win)

        for i in range(self.Enemy_index):
            self.mEnemies[i].draw(win)
