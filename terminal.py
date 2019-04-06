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
        self.not_avalible = False

    def update(self, dt):
<<<<<<< HEAD

        #self.x+=dt
        if self.not_avalible == True:
            self.x += dt
            print(self.x)
            if self.x > self.timer:
                print("reset")
                self.x = 0
                self.term_string = "Code: "
                self.not_avalible = False
=======
        pass
        # print(self.keys)
        # for nums in Keys_info:
            # print(nums)
>>>>>>> f094e4a868c91fef0cf1467ac38a5695dbab687b

    def input(self, evt, keys):
        if evt.type == pygame.KEYDOWN:
            x = evt.key
            #print(x)
            if str(x) in self.keys:
                #self.term_string = "Code: "
                self.term_string += self.keys[str(x)]
            else:
                x = "Code: Not Avalible"
                self.term_string = x
                self.not_avalible = True
            #print(x)

    def draw(self, win):
        win.blit(self.image, (0, 0, win_width, win_height))
        win.blit(self.font.render(self.term_string, True, (255, 255, 255)), (245, 170))
