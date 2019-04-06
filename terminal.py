import pygame
from config import *


class Terminal:
    def __init__(self):
        self.image = TERM
        self.font = pygame.font.SysFont("Vixar ASCI", 48)
        self.term_string = "Code: "
        self.keys = Keys_info

    def update(self, dt):
        pass
        #print(self.keys)
        #for nums in Keys_info:
            #print(nums)

    def input(self, evt, keys):
        if evt.type == pygame.KEYDOWN:
            x = evt.key
            print(x)
            self.term_string += self.keys[str(x)]
            print(x)

    def draw(self, win):
        win.blit(self.image, (0, 0, win_width, win_height))
        win.blit(self.font.render(self.term_string, True, (255, 255, 255)), (245, 170))

        # Fonts
        # Vixar ASCI
        # Quartz MS
