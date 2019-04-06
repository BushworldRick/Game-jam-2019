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
        self.frame_row = 6
        self.frame_column = 0

        # stuff for the image
        self.img = img
        self.img_w = self.img.get_width
        self.img_h = self.img.get_height

    def update(self, dt):
        self.dt = dt

        # keep on screen code
        if self.pos[0] < 0 + self.player_hitbox:
            self.pos[0] = 0 + self.player_hitbox
        if self.pos[0] > self.screenwidth - self.player_hitbox:
            self.pos[0] = self.screenwidth - self.player_hitbox
        if self.pos[1] < 0 + (self.player_hitbox * 2):
            self.pos[1] = 0 + (self.player_hitbox * 2)
        if self.pos[1] > self.screenheight - (self.player_hitbox *  2):
            self.pos[1] = self.screenheight - (self.player_hitbox * 2)

    def input(self, keys):
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

        rect = (ship_directions["framewidth"] * self.frame_column, ship_directions["frameheight"] * self.frame_row,
        ship_directions["framewidth"], ship_directions["frameheight"])

        surf.blit(self.img, (int(self.pos[0]),int(self.pos[1])), rect)
