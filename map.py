import pygame
from Player import *
from config import *
from random import randint, choice, sample
from Enemy import *
from bullet import *
from copy import deepcopy

NUM_ENEMIES = 30

class Map:
    def __init__(self,code_good):
        self.win_width = win_width
        self.win_height = win_height
        self.code_good = code_good
        self.mPreset_enemies = []
        num = len(TheEnd_dict)
        print(num)
        for i in range(NUM_ENEMIES):
            spwn_x = randint(0, win_width)
            chance = randint(0,5)
            if num > 0:
                print(num)
                if chance == 0:
                    key = choice(list(TheEnd_dict.keys()))
                    letter = TheEnd_dict[key]
                    print(key, letter, "key, letter")
                    self.mPreset_enemies.append(Enemy(spwn_x, -50, str(letter)))
                    del TheEnd_dict[key]
                    num -= 1
                else:
                    self.mPreset_enemies.append(Enemy(spwn_x, -50))
        print(num, "num before while loop")
        while num > 0:
            spwn_x = randint(0, win_width)
            print(TheEnd_dict)
            key = choice(list(TheEnd_dict.keys()))
            letter = TheEnd_dict[key]
            self.mPreset_enemies.append(Enemy(spwn_x, -50, str(letter)))
            del TheEnd_dict[key]
            num -= 1
        self.mEnemies = [deepcopy(self.mPreset_enemies[0])]
        self.Enemy_delay = 0.5
        self.Enemy_index = 1
        self.mNum_enemies = len(self.mPreset_enemies)
        self.bullet_list = []
        self.mDel_enemies = False
        self.mBoss_phase = False
        self.mAdd_phase = True
        self.hp_bar = pygame.image.load("Sprites/hp_gradient.png")
        self.mFont = pygame.font.SysFont("Times New Roman", 50)
        self.mEnemy_bullets = []
        self.mEnemy_bullet_timer = 1.5


        #player thing
        self.Player = Player((800, 600), code_good, SHIP)


    def update(self, dt, code):
        self.code_good = code
        self.mEnemy_bullet_timer -= dt
        #print(str(self.code_good) + " map class")

        if self.Enemy_index < self.mNum_enemies:
            self.Enemy_delay -= dt
            if self.Enemy_delay < 0:
                self.mEnemies.append(deepcopy(self.mPreset_enemies[self.Enemy_index]))
                self.Enemy_index += 1
                self.Enemy_delay = 0.5

        self.Player.update(dt, self.code_good)

        # print(len(self.mEnemies), "number of enemies")
        if len(self.mEnemies) > 0:
            for e in self.mEnemies:
                spwn_bullets = e.update(dt)
                if spwn_bullets:
                    self.mEnemy_bullets.append(e.attack())
                    self.mEnemy_bullet_timer = 1.5
                # print(e.mPos[1])
                if e.mPos[1] > 810:
                    self.mEnemies.remove(e)

        for group in self.mEnemy_bullets:
            for bullet in group:
                bullet[1] += bullet[2][1] * dt
                bullet[0] += bullet[2][0] * dt

        for enemy in self.mEnemies:
            if enemy.pars_y <= 8:
                self.mEnemies.remove(enemy)
                break
            for bullet in self.Player.bullet_list:
                b_x = bullet.pos[0]
                b_y = bullet.pos[1]
                e_x = enemy.mPos[0]
                e_y = enemy.mPos[1]
                a = e_x - b_x
                b = e_y - b_y
                distance = (a * a + b * b) ** 0.5
                if distance < bullet.rad + enemy.mEnemy_rad:
                    enemy.explode()
                    if enemy.pars_y == 323:
                        self.Player.bullet_list.remove(bullet)
                    break

    def reset(self):
        self.Enemy_index = 1
        self.mBoss_phase = False
        self.mAdd_phase = True
        self.Enemy_delay = 0.5
        self.mDel_enemies = False

    def input(self, evt, keys):
        self.Player.input(evt,keys)
        # print(len(self.mEnemies))
        # print(self.Enemy_index, "enemy index")
        if len(self.mEnemies) == 0:
            self.mEnemies = [deepcopy(self.mPreset_enemies[0])]
            return True, False
        return self.mBoss_phase, self.mAdd_phase

    def draw(self, win):

        self.Player.draw(win)

        for bullet_group in self.mEnemy_bullets:
            for bullet in bullet_group:
                win.blit(BULLET, (int(bullet[0]), int(bullet[1])))
                #pygame.draw.circle(win, (255, 0, 0), (int(bullet[0]), int(bullet[1])), 5)

        if len(self.mEnemies) > 0:
            for e in self.mEnemies:
                e.draw(win, self.mFont)
