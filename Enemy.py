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
        self.mEnemy_rad = 18
        self.mFrame_delay = 0.1
        self.Exploding = False

    def update(self, dt):
        self.mPos[1] += self.mRate * dt
        self.mPos[0] = math.sin(self.mPos[1] * .05) * self.mSin_width + self.mid_x

    def explode(self):
        #self.mSource_rect = pygame.Rect()
        self.Exploding = True

    def draw(self, win):
        if not self.Exploding:
            win.blit(ENEMY, (int(self.mPos[0] - (35/2)), int(self.mPos[1]) - (40/2)), (5, 10, 35, 40))
        else:
            win.blit(SHIP, (int(self.mPos[0] - (35/2)), int(self.mPos[1]) - (40/2)), (310, 323, 85, 70))
        pygame.draw.circle(win, (255, 0, 0), (int(self.mPos[0]), int(self.mPos[1]) - 5), self.mEnemy_rad, 1)
