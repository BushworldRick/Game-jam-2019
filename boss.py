import pygame
from config import *
from Player import *


class Boss:
    def __init__(self, x, y, map):
        self.position = [x, y]
        self.Map = map
        self.mHealth = 100
        self.mBoss_image = pygame.image.load("Sprites/PossibleBoss1.png")
        self.mBoss_w = self.mBoss_image.get_width()
        self.mBoss_h = self.mBoss_image.get_height()
        self.speed = 100

    def update(self, dt):
        self.Map.Player.update(dt)

        if self.position[1] < 75:
            self.position[1] += self.speed * dt

    def attack1(self):


    def input(self, evt, keys):
        self.Map.Player.input(keys)

    def draw(self, win):
        self.Map.Player.draw(win)
        win.blit(self.mBoss_image, (self.position[0] - (self.mBoss_w/2), self.position[1] - (self.mBoss_h/2)))




