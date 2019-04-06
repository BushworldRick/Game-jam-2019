import pygame
from config import *


class Terminal:
    def __init__(self):
        self.image = pygame.image.load("Sprites/futuristicScreen.jpg")
        self.font = pygame.font.SysFont("Vixar ASCI", 48)

    def update(self, dt):
        pass

    def draw(self, win, string):
        win.blit(self.image, (0, 0, win_width, win_height))
        win.blit(self.font.render(string, True, (255, 255, 255)), (245, 170))

        # Fonts
        # Vixar ASCI
        # Quartz MS
