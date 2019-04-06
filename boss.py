import pygame
from config import *
from Player import *


class Boss:
    def __init__(self, x, y, map):
        self.position = [x, y]
        self.Map = map

    def update(self, dt):
        self.Map.Player.update(dt)

    def input(self, evt, keys):
        self.Map.Player.input(keys)

    def draw(self, win):
        self.Map.Player.draw(win)




