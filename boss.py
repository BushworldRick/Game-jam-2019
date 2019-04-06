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
        self.mBullet_list = []

        self.mBullet_cooldown = 1

    def update(self, dt):
        self.Map.Player.update(dt)

        if self.position[1] < 75:
            self.position[1] += self.speed * dt

        self.mBullet_cooldown -= dt
        if self.mBullet_cooldown < 0:
            self.attack1(self.position[0] - 50, self.position[1])
            self.attack1(self.position[0] + 50, self.position[1])

        for group in self.mBullet_list:
            for bullet in group:
                bullet[1] += bullet[2][1] * dt
                bullet[0] += bullet[2][0] * dt

    def attack1(self, spwn_x, spwn_y):
        x_rate = 50
        y_rate = 150
        bullet1 = [spwn_x, spwn_y, [0, y_rate]]
        bullet2 = [spwn_x, spwn_y, [x_rate, y_rate]]
        bullet3 = [spwn_x, spwn_y, [x_rate*2, y_rate]]
        bullet4 = [spwn_x, spwn_y, [-x_rate, y_rate]]
        bullet5 = [spwn_x, spwn_y, [-x_rate*2, y_rate]]
        bullet_group = [bullet1, bullet2, bullet3, bullet4, bullet5]
        self.mBullet_list.append(bullet_group)
        self.mBullet_cooldown = 1



    def input(self, evt, keys):
        self.Map.Player.input(evt, keys)

    def draw(self, win):
        self.Map.Player.draw(win)
        for bullet_group in self.mBullet_list:
            for bullet in bullet_group:
                pygame.draw.circle(win ,(255, 0, 0), (int(bullet[0]), int(bullet[1])), 5,)
        win.blit(self.mBoss_image, (self.position[0] - (self.mBoss_w/2), self.position[1] - (self.mBoss_h/2)))




