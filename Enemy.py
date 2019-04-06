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
        self.Exploding_frameh = 100
        self.pars_y = 323

    def update(self, dt):
        if not self.Exploding:
            self.mPos[1] += self.mRate * dt
            self.mPos[0] = math.sin(self.mPos[1] * .05) * self.mSin_width + self.mid_x
        elif self.Exploding:
            self.mFrame_delay -= dt
            if self.mFrame_delay < 0:
                self.pars_y -= self.Exploding_frameh
                self.mFrame_delay = 0.1

    def explode(self):
        #self.mSource_rect = pygame.Rect()
        self.Exploding = True

    def draw(self, win):
        if not self.Exploding:
            win.blit(ENEMY, (int(self.mPos[0] - (35/2)), int(self.mPos[1]) - (40/2)), (5, 10, 35, 40))
        else:
            print(self.pars_y)
            win.blit(SHIP, (int(self.mPos[0] - (85/2)), int(self.mPos[1]) - (self.Exploding_frameh/2)), (310, self.pars_y, 85, self.Exploding_frameh))
        #pygame.draw.circle(win, (255, 0, 0), (int(self.mPos[0]), int(self.mPos[1]) - 5), self.mEnemy_rad, 1)
