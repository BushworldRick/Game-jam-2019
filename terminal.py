import pygame
from config import *


class Terminal:
    def __init__(self):
        self.image = TERM
        self.font = pygame.font.SysFont("Vixar ASCI", 48)
        self.term_string = "Code: "
        self.keys = Keys_info
        self.timer = 1
        self.x = 0
        self.not_available = False      # checking for wrong key press thing
        self.solutions = ["Code: the end","Code: theend"]
        self.code_good = False
        self.locked_input = ''

    def update(self, dt):

        # self.x += dt
        if self.not_available:
            self.x += dt
            print(self.x)
            if self.x > self.timer:
                print("reset")
                self.x = 0
                self.term_string = "Code: "
                self.not_available = False

        for s in self.solutions:
            if s == self.locked_input:
                self.code_good = True
                #print(self.code_good)
        return self.code_good


    def input(self, evt, keys):
        if evt.type == pygame.KEYDOWN:
            x = evt.key
            print(x)
            if str(x) in self.keys:
                # self.term_string = "Code: "
                self.term_string += self.keys[str(x)]
            else:
                x = "Code: Not Available"
                self.term_string = x
                self.not_available = True
            if evt.key == pygame.K_RETURN:
                self.not_available = False
                self.locked_input = "Code: the end"


    def draw(self, win):
        win.blit(self.image, (0, 0, win_width, win_height))
        win.blit(self.font.render(self.term_string, True, (255, 255, 255)), (245, 170))
