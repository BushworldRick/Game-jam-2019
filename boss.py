import pygame
from config import *
from Player import *


class Boss:
    def __init__(self, x, y, map):
        self.position = [x, y]
        self.Map = map
        self.mHealth = 1000
        self.mBoss_image = pygame.image.load("Sprites/PossibleBoss1.png")
        self.mBoss_w = self.mBoss_image.get_width()
        self.mBoss_h = self.mBoss_image.get_height()
        self.speed = 100
        self.mBullet_list = []
        self.mBoss_timer = 10
        self.mBoss_phase = True
        self.mAdd_phase = False
        self.mBullet_cooldown = 1

        # text box / timer stuff
        self.print1 = False
        self.font = pygame.font.SysFont("Bahnschrift", 16)
        self.print1_text = "Hah i'm gonona get you fool, ya fool!"
        self.print2 = False
        self.print2_text = "Figure out the code to leave fool, ya fool!"
        self.x = 0
        self.text_timer = 1.5
        self.text_box = pygame.Surface((315,50))

    def update(self, dt):
        self.mBoss_timer -= dt
        self.Map.Player.update(dt)

        if self.print1 == True:
            #print("it works")
            self.x += dt
            if self.x > self.text_timer:
                self.print1 = False
                self.x = 0
        if self.print2 == True:
            #print("it works")
            self.x += dt
            if self.x > self.text_timer:
                self.print2 = False
                self.x = 0

        if self.mBoss_timer > 0:        #this is where the boss stops
            if self.position[1] < 75:
                self.position[1] += self.speed * dt
                self.print1 = True

        if self.mBoss_timer <= 0:
            self.position[1] -= self.speed * dt
            self.print2 = True

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

        if self.position[1] < -300:
            self.position[1] = -299
            return False, True

        return self.mBoss_phase, self.mAdd_phase

    def reset(self):
        self.mBullet_list = []
        self.position[1] = -300
        self.mAdd_phase = False
        self.mBoss_phase = True
        self.mBoss_timer = 10

    def draw(self, win):

        self.Map.Player.draw(win)
        for bullet_group in self.mBullet_list:
            for bullet in bullet_group:
                pygame.draw.circle(win, (255, 0, 0), (int(bullet[0]), int(bullet[1])), 5)
        win.blit(self.mBoss_image, (self.position[0] - (self.mBoss_w/2), self.position[1] - (self.mBoss_h/2)))

        pygame.draw.rect(win, (255, 255, 0), (15, 15, 200, 10), 1)
        pygame.draw.rect(win, (255, 255, 0), (15, 15, int(self.mHealth/5), 10))

        if self.print1 == True:
            win.blit(self.text_box,(self.position[0],self.position[1] + 250))
            self.text_box.fill((255,255,255))
            self.text_box.blit(self.font.render(self.print1_text, True, (0,0,0)),(15,15))
            #self.chest_screen.blit(self.font.render(str(text[0]), True, (0, 0, 0)),(35, 20))

        if self.print2 == True:
            win.blit(self.text_box,(self.position[0],self.position[1] + 250))
            self.text_box.fill((255,255,255))
            self.text_box.blit(self.font.render(self.print2_text, True, (0,0,0)),(15,15))
