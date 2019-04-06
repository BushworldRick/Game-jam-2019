import pygame
import random
from config import *


class Boss:
    def __init__(self, pos):
        self.mPos = [pos[0], pos[1]]
        self.mSin_width = random.randint(30, 75)
        self.mid_x = pos[0]
        self.Speed = 0.1
        self.mRate = 100

    def update(self, dt):
        self.mPos[1] += self.mRate * dt
        self.mPos[0] = math.sin(self.mPos[1] * .05) * self.mSin_width + self.mid_x

    def input(self):
        pass

    def draw(self, win):
        pygame.draw.circle(win, (255, 0, 0), (int(self.mPos[0]), int(self.mPos[1])), 5,)
