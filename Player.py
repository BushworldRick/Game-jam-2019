import pygame
from config import *

class Player:
    def __init__(self,screen_dems, img = None):

        # screen dimensions
        self.screenwidth = screen_dems[0]
        self.screenheight = screen_dems[1]

        # player stuff
        self.pos = [self.screenwidth//2,500]
        self.speed = 150
        self.player_hitbox = 15
        self.bullets = []   # bullet class objects

        # stuff for the image
        self.img = img
        self.img_w = self.img.get_width
        self.img_h = self.img.get_height


    def update(self,dt):
        self.dt = dt

        # keep on screen code
        if self.pos[0] < 0:
            self.pos[0] = 0 + self.player_hitbox
        if self.pos[0] > self.screenwidth:
            self.pos[0] = self.screenwidth - self.player_hitbox
        if self.pos[1] < 0:
            self.pos[1] = 0 + self.player_hitbox
        if self.pos[1] > self.screenheight:
            self.pos[1] = self.screenheight - self.player_hitbox


    def input(self,keys):
        # Moving player_ship
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.pos[0] -= self.speed * self.dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.pos[0] += self.speed * self.dt
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.pos[1] -= self.speed * self.dt
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.pos[1] += self.speed * self.dt

    def draw(self,surf):
        # temorary player
        pygame.draw.circle(surf, (0,255,0), (int(self.pos[0]), int(self.pos[1])), 15)
