import pygame
import math
import random
from config import *


class Enemy:
    def __init__(self, x, y, letter=None):

        self.mLetter = letter
        self.mPos = [x, y]
        self.mSin_width = random.randint(30, 75)
        self.mid_x = x
        self.Speed = 0.1
        self.mRate = 100

    def update(self, dt):
        self.mPos[1] += self.mRate * dt
        self.mPos[0] = math.sin(self.mPos[1] * .05) * self.mSin_width + self.mid_x

    def draw(self, win):
        win.blit(ENEMY, (int(self.mPos[0]), int(self.mPos[1])))
