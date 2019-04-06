import pygame
from config import *


class Terminal:
    def __init__(self):
        self.image = pygame.load.image("Sprites/futuristicScreen")
        self.font = pygame.Font.SysFont("Vixar ASCI")

    def update(self, dt):
        pass

    def draw(self, win, string):
        win.blit(self.image, (0, 0, win_width, win_height))
        win.blit(self.font.render(string, True, (0, 0, 0)), (245, 170))

        # Fonts
        # Vixar ASCI
        # Quartz MS
